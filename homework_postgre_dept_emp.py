import psycopg2
import csv

postgres_connection = psycopg2.connect(
    user = "postgres",
    host = "localhost",
    port = "5432",
    password = "992907",
    database = "data-analytics-engineer"
)

postgres_cursor = postgres_connection.cursor()

create_table_sql = f"""
   CREATE TABLE IF NOT EXISTS dept_emp(
       emp_no SERIAL PRIMARY KEY,
       dept_no VARCHAR,
       from_date TIMESTAMP WITH TIME ZONE,
       to_date TIMESTAMP WITH TIME ZONE
   )
"""
postgres_cursor.execute(create_table_sql)
with open('departments.csv', newline='') as csv_file:
    file_reader = csv.DictReader(csv_file)
    for row in file_reader:
        insert_data_sql = f"""
           INSERT INTO dept_emp
           (emp_no, dept_no, from_date, to_date)
           VALUES
           ('{row['emp_no']}', '{row['dept_no']}', '{row['from_date']}', '{row['to_date']}')
        """
        postgres_cursor.execute(insert_data_sql)

postgres_connection.commit()
postgres_cursor.close()
postgres_connection.close()



