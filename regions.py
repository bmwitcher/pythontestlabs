import boto3 as aws

ec2_client = aws.client('ec2')

response = ec2_client.describe_regions()

regions = response['Regions']
#print(regions)
for region in regions:
    print(region['RegionName'])