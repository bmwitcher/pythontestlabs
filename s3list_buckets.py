import boto3

def lists3_buckets():
    session = boto3.Session(region_name='us-east-1')
    s3client = session.client('s3')
    bucket_list = s3client.list_buckets()
    #print(bucket_list['Buckets'])
    for bucket in bucket_list['Buckets']:
        print(f"The bucket name is: {bucket['Name']}, bucket creationdate is: {bucket['CreationDate']}")

    return

lists3_buckets()