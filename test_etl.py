import csv
import os

import psycopg2.extras
from google.cloud import storage, bigquery
from google.oauth2.service_account import Credentials

postgres_connection = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="992907",
    database="data-analytics-engineer"
)

postgres_cursor = postgres_connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

postgres_sql = "SELECT * FROM employees"

postgres_cursor.execute(postgres_sql)

print(postgres_cursor.description)
fieldnames = []
for column in postgres_cursor.description:
    fieldnames.append(column.name)

file_no = 1
file_name = f"{file_no}.csv"
file = open(file_name, "w+", newline="")
csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
csv_writer.writeheader()

service_account_file = "C:/Users/HP/Documents/data-analytics-engineer-bigquery.json"
credentials = Credentials.from_service_account_file(service_account_file)
storage_client = storage.Client(credentials=credentials)

bucket_name = "data-analytics-engineer-example-quyentran"
bucket = storage_client.bucket(bucket_name)

count = 0
for row in postgres_cursor:
    row_dict = dict(row)
    row_dict["hire_date"] = row_dict["hire_date"].strftime("%Y-%m-%d")
    csv_writer.writerow(row_dict)

    count = count + 1

    if count >= 200:
        file.close()

        upload_filename = f"data/employees/{file_name}"
        blob = bucket.blob(upload_filename)
        blob.upload_from_filename(file_name)
        print(f"finish uploading {file_name} - Remove file {file_name}")
        os.remove(file_name)

        file_no += 1
        file_name = f"{file_no}.csv"
        file = open(file_name, "w+", newline="")
        csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
        csv_writer.writeheader()

        count = 0

file.close()
upload_filename = f"data/employees/{file_name}"
blob = bucket.blob(upload_filename)
blob.upload_from_filename(file_name)
os.remove(file_name)

table_id = "data-analytics-engineer.sql_practice.employees"

job_config = bigquery.LoadJobConfig(
   source_format=bigquery.SourceFormat.CSV,
   skip_leading_rows=1,
   write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)
bigquery_client = bigquery.Client()
job = bigquery_client.load_table_from_uri(
   source_uris="gs://data-analytics-engineer-example-quyentran/data/employees/*.csv",
   destination=table_id,
   job_config=job_config
)
job.result()

postgres_cursor.close()
postgres_connection.close()
