import boto3
import os

s3 = boto3.client('s3')

def upload_files(directory, bucket_name):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"Subindo {file}...")
            s3.upload_file(file_path, bucket_name, file)

if __name__ == "__main__":
    MY_BUCKET = "teste-directory"
    upload_files('.', MY_BUCKET)