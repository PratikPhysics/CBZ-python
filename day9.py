# make an ec2 instance

import boto3

# Initialize a session using Amazon EC2
ec2 = boto3.client('ec2')

# Create an EC2 instance
response = ec2.run_instances(
    ImageId='ami-04b4f1a9cf54c11d0',  # Replace with your desired AMI ID
    InstanceType='t2.micro',          # Instance type
    MinCount=1,                       # Minimum number of instances to launch
    MaxCount=1,                       # Maximum number of instances to launch
    KeyName='my-key-pair',          # Replace with your key pair name
    SecurityGroupIds=['sg-0a40438dad67ab102'],  # Replace with your security group ID
    SubnetId='subnet-0715fa2c9541da8ab',       # Replace with your subnet ID
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'MyEC2Instance'
                },
            ]
        },
    ]
)

# Print the instance ID
instance_id = response['Instances'][0]['InstanceId']
print(f"EC2 Instance Created with ID: {instance_id}")



#-------------------❌-----------❌-----------❌-----------❌-----------❌-----------❌

# make a s3 bucket


import boto3

# Initialize a session using Amazon S3
s3 = boto3.client('s3')

# Define the bucket name and region
bucket_name = 'cloudbliztkibucket'
region = 'us-east-1'  # No need for CreateBucketConfiguration here

try:
    # Create the bucket (without specifying CreateBucketConfiguration for us-east-1)
    response = s3.create_bucket(Bucket=bucket_name)

    print(f"Bucket '{bucket_name}' created successfully!")
    print(response)

except Exception as e:
    print(f"Error occurred: {e}")


#-------------❌--------❌--------❌--------❌--------❌--------❌--------❌--------❌

# create an IAM user


import boto3
import botocore.exceptions
 
def create_iam_user(username):
    iam = boto3.client('iam')
    try:
        response = iam.create_user(UserName=username)
        print(f"User '{username}' created successfully.")
        return response['User']['UserName']
    except botocore.exceptions.ClientError as e:
        print(f"Error creating user: {e}")
        return None
 
def create_iam_group(group_name):
    iam = boto3.client('iam')
    try:
        response = iam.create_group(GroupName=group_name)
        print(f"Group '{group_name}' created successfully.")
        return response['Group']['GroupName']
    except botocore.exceptions.ClientError as e:
        print(f"Error creating group: {e}")
        return None
 
def add_user_to_group(username, group_name):
    iam = boto3.client('iam')
    try:
        iam.add_user_to_group(UserName=username, GroupName=group_name)
        print(f"User '{username}' added to group '{group_name}'.")
    except botocore.exceptions.ClientError as e:
        print(f"Error adding user to group: {e}")
 
def attach_admin_policy(group_name):
    iam = boto3.client('iam')
    policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"
    try:
        iam.attach_group_policy(GroupName=group_name, PolicyArn=policy_arn)
        print(f"Admin policy attached to group '{group_name}'.")
    except botocore.exceptions.ClientError as e:
        print(f"Error attaching policy: {e}")
 
def main():
    username = "newIAMUser"
    group_name = "AdminGroup"
 
  
    user = create_iam_user(username)
    group = create_iam_group(group_name)
    if user and group:
        add_user_to_group(username, group_name)
        attach_admin_policy(group_name)
if __name__ == "__main__":
    main()


