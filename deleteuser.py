import boto3

iam = boto3.client('iam')

response = iam.detach_user_policy(
    UserName='pythontestuser',
    PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
)

response = iam.delete_user(
    UserName='pythontestuser'
)