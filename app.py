from flask import Flask, render_template, request, session, redirect, url_for, flash
from snowflake.sqlalchemy import URL
from sqlalchemy import create_engine
import pandas as pd
import re
import logging

app = Flask(__name__)
app.secret_key = 'snowflake'
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['user']
        password = request.form['password']
        account = request.form['account']
        try:
            engine = create_engine(URL(
                user=user,
                password=password,
                account=account,
                schema='PUBLIC',
                warehouse=request.form.get('warehouse', ''),
                database=request.form.get('database', ''),
                role=request.form.get('role', ''),
                ocsp_fail_open=False
            ))
            connection = engine.connect()
            connection.close()
            session.update({
                'user': user,
                'password': password,
                'account': account,
                'warehouse': request.form.get('warehouse', ''),
                'database': request.form.get('database', '')
            })
            return redirect(url_for('analyze_cte'))
        except Exception as e:
            logging.error("Connection error: %s", e)
            flash("Failed to connect to Snowflake: " + str(e))
            return render_template('login.html'), 400
    return render_template('login.html')

def parse_ctes(sql_query):
    ctes = {}
    main_query = sql_query
    cte_pattern = re.compile(r"(\w+)\s+AS\s+\(([^;]+?)\)(?:,|WITH|$)", re.IGNORECASE | re.DOTALL)
    matches = cte_pattern.findall(sql_query)
    for match in matches:
        cte_name, cte_body = match
        ctes[cte_name.strip()] = cte_body.strip()
    return ctes, main_query

@app.route('/analyze_cte', methods=['GET', 'POST'])
def analyze_cte():
    if 'user' not in session:
        flash("Please log in to access this page.")
        return redirect(url_for('login'))

    if request.method == 'POST':
        schema = request.form['schema']
        sql_query = request.form['sql_query']
        ctes, _ = parse_ctes(sql_query)
        results = {}
        try:
            engine = create_engine(URL(
                user=session['user'],
                password=session['password'],
                account=session['account'],
                warehouse=session.get('warehouse'),
                database=session.get('database'),
                schema=schema,
                ocsp_fail_open=True
            ))
            connection = engine.connect()

            full_cte_definitions = ', '.join([f"{name} AS ({query})" for name, query in ctes.items()])
            for cte_name in ctes.keys():
                query = f"WITH {full_cte_definitions} SELECT * FROM {cte_name}"
                logging.debug("Executing query: %s", query)
                df = pd.read_sql(query, connection)
                duplicates = df[df.duplicated(keep=False)]
                results[cte_name] = {
                    'row_count': len(df),
                    'duplicate_count': len(duplicates),
                    'duplicates': duplicates.to_html(classes='data', border=0),
                    'result': df.head().to_html(classes='data', border=0)
                }
            connection.close()
        except Exception as e:
            logging.error("Failed to execute CTE: %s", e)
            flash(f"Failed to execute CTE: {e}")
        return render_template('cte_analysis.html', results=results, schema=schema, sql_query=sql_query)

    return render_template('cte_analysis.html')

if __name__ == '__main__':
    app.run(debug=True)
