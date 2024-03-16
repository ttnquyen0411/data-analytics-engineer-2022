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
   CREATE TABLE IF NOT EXISTS staff_locations_view(
       staff_id SERIAL PRIMARY KEY,
       first_name VARCHAR,
       last_name VARCHAR,
       location VARCHAR
   )
"""
postgres_cursor.execute(create_table_sql)

with open('staff_locations_view (1).csv', newline='') as csv_file:
    file_reader = csv.DictReader(csv_file, delimiter=',')
    for row in file_reader:
        insert_data_sql = f"""
           INSERT INTO staff_locations_view
           (staff_id, first_name, last_name, location)
           VALUES
           ('{row['staff_id']}', '{row['first_name']}', '{row['last_name']}', '{row['location']}')
        """
        postgres_cursor.execute(insert_data_sql)

postgres_connection.commit()
postgres_cursor.close()
postgres_connection.close()
