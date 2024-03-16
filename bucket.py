from google.cloud import storage
from google.oauth2.service_account import Credentials

service_account_file = "C:\\Users\\HP\\Documents\\Project\\Data-analytics-engineer\\data-analytics-engineer-7a8217e7b516.json"
credentials = Credentials.from_service_account_file(service_account_file)
storage_client = storage.Client(credentials=credentials)

# The name for the new bucket
bucket_name = "data-analytics-engineer-example-quyentran"
# Creates the new bucket
bucket = storage_client.create_bucket(bucket_name)
if not bucket.exists():
    bucket = storage_client.create_bucket(bucket_name)
    print(f"Bucket {bucket_name} created.")
