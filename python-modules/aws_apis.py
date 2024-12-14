import boto3

def list_iam_users():
    iam = boto3.client('iam')
    resp = iam.list_users()
    user_list =[]
    for user in resp['Users']:
        user_list.append(user['UserName'])
    return user_list

"""def list_ec2_id():    
    ec2 = boto3.client('ec2', region_name='us-west-1')
    resp = ec2.describe_instances()
    instance_list = []
    for inst in resp['Reservations']:
        for i in inst['Instances']:
            instance_list.append(i['InstanceId'])
    return instance_list

def stop_instance(instances):
    ec2 = boto3.client('ec2', region_name='us-west-1')
    ec2.stop_instances(InstanceIds=instances)

def start_instance(instances):
    ec2 = boto3.client('ec2', region_name='us-west-1')
    ec2.start_instances(InstanceIds=instances)
"""
    