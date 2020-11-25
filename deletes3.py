
import logging
import boto3
from botocore.exceptions import ClientError

client = boto3.client('s3')

client.delete_object(
    Bucket='pythonwitchertest',
    Key='levelup.jpg',
)


client.delete_bucket(
    Bucket='pythonwitchertest',
)
