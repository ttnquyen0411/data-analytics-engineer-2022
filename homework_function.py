import psycopg2
import psycopg2.extras

def extract_postgres_to_gcs(table_name, bucket_name, filename_format):
    # Write code here to get  data from table_name in postgres
    # Then upload extracted data from table name to bucket with filename format

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

    file_name = filename_format.format(file_no=file_no)
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
    upload_filename = filename_format.format(file_no=file_no)
    blob = bucket.blob(upload_filename)
    blob.upload_from_filename(file_name)
    os.remove(file_name)

    table_id = "data-analytics-engineer.sql_practice.employees"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

def load_to_bigquery(source_uris, dataset, table_name, write_disposition):
    # Write the code to load data from source_uris to table table_name in dataset with write_disposition
    # write disposition must be WRITE_EMPTY, WRITE_APPEND OR WRITE_TRUNCATE, other will print error

table_name = "employees"
# Declare bucket_name to upload data
bucket_name = "data-analytics-engineer-example-quyentran"
# Make variable filename_format here with contain table_name
filename_format = f"postgres/data/{table_name}/{{file_no}}.csv"

extract_postgres_to_gcs(
    table_name=table_name,
    bucket_name=bucket_name,
    filename_format=filename_format
)

# generate source_uirs variable base on bucket_name and file_name_format
source_uris = ""

# Declare dataset
dataset = ""
# Name of table in bigquery to load data into
bigquery_table_name = ""

# declare write_disposition
bigquery_write_disposition = ""
load_to_bigquery(
    source_uris=source_uris,
    dataset=bucket_name,
    table_name=bigquery_table_name,
    write_disposition=bigquery_write_disposition
)