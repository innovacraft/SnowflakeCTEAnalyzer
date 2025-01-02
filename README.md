# Snowflake CTE Analyzer

The Snowflake CTE Analyzer is a Flask-based web application designed to help users write, analyze, and optimize SQL Common Table Expressions (CTEs) within Snowflake databases. It provides a user-friendly interface for executing SQL CTEs and offers detailed analytics on each part of the query, including performance metrics and duplicate detection across multiple CTEs.

<img width="1208" alt="Screenshot 2025-01-02 at 4 45 08 PM" src="https://github.com/user-attachments/assets/810d6a8f-794c-4715-a9c8-47407b275432" />

## Features

- **Interactive Web Interface**: Provides a simple and intuitive web interface for entering and executing CTEs.
- **Advanced Query Analysis**: Analyzes complex queries with multiple CTEs, displaying results for each CTE independently.
- **Duplicate Detection**: Identifies and reports duplicate records within each CTE, helping to ensure data accuracy.
- **Schema Flexibility**: Allows users to specify different schemas, facilitating queries across various database segments.

## Installation

To get started with the Snowflake CTE Analyzer, follow these installation steps:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/SnowflakeCTEAnalyzer.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd SnowflakeCTEAnalyzer
   ```

3. **Install required Python packages:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install required Python packages:**
```bash
pip install -r requirements.txt
```

## Usage

Follow these steps to analyze your SQL CTEs:

**Login:** Start by logging in with your Snowflake credentials (if authentication is enabled).

<img width="681" alt="Screenshot 2025-01-02 at 4 38 25 PM" src="https://github.com/user-attachments/assets/99d77bc3-403f-4941-828e-4396e433df62" />

**Enter the SQL Query:** Type your CTE query into the designated text area.

**Select the Schema:** Choose the appropriate schema for your query execution.

<img width="1602" alt="Screenshot 2025-01-02 at 4 41 42 PM" src="https://github.com/user-attachments/assets/26fb7607-69a6-43db-be68-394eb0d42a2c" />

**Analyze:** Click on "Analyze CTE" to submit your query and view the analysis, including details like row counts, duplicate records, and execution metrics.

<img width="1608" alt="Screenshot 2025-01-02 at 4 42 27 PM" src="https://github.com/user-attachments/assets/505ebeb6-fe43-466c-918c-4fa19e90e865" />

## Future Scope

**Support for Multiple Databases:** Plans to extend functionality to other database platforms like AWS Redshift and Google BigQuery.
**Automated Query Optimization:** Future updates may include automated suggestions for query optimization based on analysis results.
**Security Enhancements:** Implementing advanced security measures for enterprise usage.






