import boto3
import random

userinput = input("Please enter the username you would like to create: ")
userid = userinput + str(random.randint(10,99))
ec2readonly = 'arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess' #aws managed arn from AWS console

def newuser(userid):
    iam = boto3.client('iam')
    response = iam.create_user(UserName=userid)   #boto3 docs say username is the only required field
    try:
        print(f'{userid} has been created successfully')
    except:
        print(f'{userid} did not complete successfully, please check your function and try again')
    return

def create_user_accesskeys(userid):
    iam = boto3.client('iam')
    response = iam.create_access_key(UserName=userid)
    try:
        print(f"Access Key ID: {response['AccessKey']['AccessKeyId']}")
        print(f"Secret Key ID: {response['AccessKey']['SecretAccessKey']}")
    except:
        print(f'{userid} did not complete successfully, please check your function and try again')
    return

def attach_userpolicy(userid, PolicyArn=ec2readonly):
    iam = boto3.client('iam')
    response = iam.attach_user_policy(UserName=userid,PolicyArn=ec2readonly)
    try:
        print(f'Policy has been applied to {userid} successfully')
    except:
        print(f'Policy was not applied, please check your function and try again')
    finally:
        print(f'This FUNCTION HAS COMPLETED, PLEASE VERIFY VIA AWS CONSOLE')

newuser(userid)
create_user_accesskeys(userid)
attach_userpolicy(userid,PolicyArn=ec2readonly)