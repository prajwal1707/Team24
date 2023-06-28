import boto3


def fetch_ec2_instances():

    # Set up AWS credentials (replace with your own credentials)

    aws_access_key_id = 'AKIA4IDJY73SLSR3NDE5'

    aws_secret_access_key = '5jk457dvtzPCC+9xZdKhNiCe6wbESbnx+kcsU3iM'


    # Set up the AWS region

    aws_region = 'ap-northeast-1'  # Replace with your desired region code


    # Initialize the AWS SDK

    session = boto3.Session(

        aws_access_key_id=aws_access_key_id,

        aws_secret_access_key=aws_secret_access_key,

        region_name=aws_region

    )

    ec2_client = session.client('ec2')


    # Fetch EC2 instances

    response = ec2_client.describe_instances()


    # Process and print instance information

    for reservation in response['Reservations']:

        for instance in reservation['Instances']:

            instance_id = instance['InstanceId']

            instance_type = instance['InstanceType']

            private_ip = instance['PrivateIpAddress']

            print(f"Instance ID: {instance_id}, Instance Type: {instance_type}, Private IP: {private_ip}")


# Call the function to fetch EC2 instance data

fetch_ec2_instances()


import sqlite3
from datetime import datetime 

# Initialize the SQLite database
conn = sqlite3.connect('aws_resources.db')
cursor = conn.cursor()

def create_table():
   # Create a table to store AWS resources
   cursor.execute('''CREATE TABLE IF NOT EXISTS resources
                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     resource_type TEXT,
                     resource_name TEXT,
                     region TEXT,
                     details TEXT)''')
   conn.commit()

def insert_resource(resource_type, resource_name, region):
   # Insert a resource into the database
   cursor.execute('''INSERT INTO resources
                     (resource_type, resource_name, region)
                     VALUES (?, ?, ?)''',
                  (resource_type, resource_name, region))
   conn.commit()

def fetch_s3_buckets():
   # Fetch S3 buckets
   s3_client = boto3.client('s3')
   response = s3_client.list_buckets()

   for bucket in response['Buckets']:
       bucket_name = bucket['aiteam24']
       #creation_date = bucket['2023-June-28,  10:37:21 '].strftime("%Y-%m-%d %H:%M:%S")
       region = 'ap-northeast-1'  # S3 buckets are not region-specific
       #details = f"Creation Date: {creation_date}"
       insert_resource('S3 Bucket', bucket_name, region)
"""

def fetch_rds_instances():
   # Fetch RDS instances
   rds_client = boto3.client('rds')
   response = rds_client.describe_db_instances()

   for instance in response['DBInstances']:
       instance_identifier = instance['DBInstanceIdentifier']
       engine = instance['Engine']
       status = instance['DBInstanceStatus']
       endpoint = instance['Endpoint']['Address']
       region = instance['AvailabilityZone'][:-1]
       details = f"Engine: {engine}, Status: {status}, Endpoint: {endpoint}"
       insert_resource('RDS Instance', instance_identifier, region, details)

def fetch_auto_scaling_groups():
   # Fetch EC2 Auto Scaling groups
   autoscaling_client = boto3.client('autoscaling')
   response = autoscaling_client.describe_auto_scaling_groups()

   for group in response['AutoScalingGroups']:
       group_name = group['AutoScalingGroupName']
       launch_config = group['LaunchConfigurationName']
       desired_capacity = group['DesiredCapacity']
       region = group['AvailabilityZones'][0][:-1]
       details = f"Launch Configuration: {launch_config}, Desired Capacity: {desired_capacity}"
       insert_resource('Auto Scaling Group', group_name, region, details)

def fetch_dynamodb_tables():
   # Fetch DynamoDB tables
   dynamodb_client = boto3.client('dynamodb')
   response = dynamodb_client.list_tables()

   for table_name in response['TableNames']:
       provisioned_capacity = dynamodb_client.describe_table(TableName=table_name)['Table']['ProvisionedThroughput']
       region = 'N/A'  # DynamoDB tables are not region-specific
       details = f"Provisioned Capacity: {provisioned_capacity}"
       insert_resource('DynamoDB Table', table_name, region, details)
"""

# Create the resources table
create_table()

# Fetch and track AWS resources
fetch_s3_buckets()
"""fetch_rds_instances()
fetch_auto_scaling_groups()
fetch_dynamodb_tables()"""

# Close the database connection
conn.close()


