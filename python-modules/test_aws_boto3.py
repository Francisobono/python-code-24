import boto3

iam = boto3.client('iam')
resp = iam.list_users()
for user in resp['Users']:
    print(user['UserName'])