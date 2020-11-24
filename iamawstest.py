import boto3

iam = boto3.client('iam')

response = iam.create_user(
    UserName='pythontestuser'
)

response = iam.attach_user_policy(
    UserName='pythontestuser',
    PolicyArn='arn:aws:iam::aws:policy/AmazonEC2FullAccess'
)
