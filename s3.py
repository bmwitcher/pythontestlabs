import boto3

s3 = boto3.resource('s3')
client = boto3.client('s3')

client.create_bucket(Bucket='pythonwitchertest')
# s3.Object('pythonwitchertest','levelup.jpg').upload_file(Filename='/Users/Bryant/Desktop/awspythontest/levelup.jpg')

client.put_object(
    ACL='public-read',
    Bucket='pythonwitchertest',
    Key='levelup.jpg',
)