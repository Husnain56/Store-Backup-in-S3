"""
Script to create a s3 bucket and store file from local storage to AWS S3
"""
import boto3

bucket_name = "backup-storage-husnain-20250711" #Enter any unique name here or use pre existing bucket 
region = "us-east-2" #Enter your own region
s3 = boto3.resource("s3", region_name=region)

def create_bucket(s3,bucket_name,region):
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )
    print("Bucket Created Successfully")

def upload_backup(s3,file_name,bucket_name,key_name):
    data = open(file_name, 'rb') #convert data to binary 
    s3.Bucket(bucket_name).put_object(Key=key_name, Body=data)
    print("Backup uploaded successfully")


create_bucket(s3,bucket_name,region) #No need to run this function if you are using pre existing S3 bucket

file_path = "File Path here" #Copy path to your file here
file_name = "my-backup.zip" #You can choose a different name
upload_backup(s3,file_name,bucket_name,file_name) 
