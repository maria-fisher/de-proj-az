from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from azure.identity import DefaultAzureCredential
import os

# Define the Azure Storage account URL
account_url = "https://envsensorstorageacct.blob.core.windows.net"

# Create an instance of DefaultAzureCredential
default_credential = DefaultAzureCredential()

# Create a BlobServiceClient object
blob_service_client = BlobServiceClient(account_url=account_url, credential=default_credential)

# Define the local folder path where your CSV files are located
local_folder_path = "./data"

# Define the name of your Azure Blob Storage container
container_name = "envsensorstorageacct"

# Create a ContainerClient object
container_client = blob_service_client.get_container_client(container_name)

# List all files in the local folder
for file_name in os.listdir(local_folder_path):
    local_file_path = os.path.join(local_folder_path, file_name)

    # Create a blob client using the file name as the blob name
    blob_client = container_client.get_blob_client(blob=file_name)

    print(f"\nUploading {file_name} to Azure Storage as blob...")
    
    # Upload the file to Azure Storage
    with open(local_file_path, "rb") as data:
        blob_client.upload_blob(data, overwrite=True)

print("Upload completed successfully.")
