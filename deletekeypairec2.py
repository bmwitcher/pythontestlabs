import boto3

client = boto3.client('ec2')


response = client.terminate_instances(
    InstanceIds=[
        'i-0ab6a91ca22874576',
    ],
    DryRun=False
)


response = client.delete_key_pair(
    KeyName='pythontestkeypair',
)

print(response)

