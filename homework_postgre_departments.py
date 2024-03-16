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
   CREATE TABLE IF NOT EXISTS departments(
       dept_no VARCHAR,
       dept_name VARCHAR
   )
"""
postgres_cursor.execute(create_table_sql)
with open('departments.csv', newline='') as csv_file:
    file_reader = csv.DictReader(csv_file)
    for row in file_reader:
        insert_data_sql = f"""
           INSERT INTO departments
           (dept_no, dept_name)
           VALUES
           ('{row['dept_no']}', '{row['dept_name']}')
        """
        postgres_cursor.execute(insert_data_sql)

postgres_connection.commit()
postgres_cursor.close()
postgres_connection.close()



