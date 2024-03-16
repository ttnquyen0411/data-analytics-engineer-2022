from google.cloud import storage
from google.oauth2.service_account import Credentials

service_account_file = "C:/Users/HP/Documents/data-analytics-engineer-bigquery.json"
credentials = Credentials.from_service_account_file(service_account_file)

storage_client = storage.Client(credentials=credentials)
bucket_name = "data-analytics-engineer-example-quyentran"
bucket = storage_client.create_bucket(bucket_name)

file_name = "./employees.csv"  # path of local file
upload_filename = "data/employees.csv"  # the name of blob
blob = bucket.blob(upload_filename)
blob.upload_from_filename(file_name)

print(f"File {blob.name} is uploaded.")