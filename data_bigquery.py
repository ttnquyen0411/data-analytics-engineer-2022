table_id = "data-analytics-engineer.sql_practice.employees"
job_config = bigquery.LoadJobConfig(
   source_format=bigquery.SourceFormat.CSV,
   skip_leading_rows=1,
   autodetect=True,
   write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
)
with open("employees.csv", "rb") as source_file:
   job = client.load_table_from_file(source_file, table_id, job_config=job_config)
job.result()  # Waits for the job to complete.
table = client.get_table(table_id)  # Make an API request.
print(
   "Loaded {} rows and {} columns to {}".format(
       table.num_rows, len(table.schema), table_id
   )
)