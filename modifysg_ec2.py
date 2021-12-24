import boto3

#ec2_id = input(f'What is the instanceid of your ec2 instance?: ')
#sg_id = input(f'What is the security group id if your isolation security group?: ')

ec2_client=boto3.client("ec2")
ec2_client.modify_instance_attribute(InstanceId='string', Groups='string')