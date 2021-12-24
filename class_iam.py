import boto3 as aws
import random


class aws_iam:
    ### CLASS INSTANCE LEVEL METHODS/FUNCTIONS ###
    def __init__(self, userid, PolicyArn):
        self.userid    = userid
        self.PolicyArn = ec2readonly

    def newuser(userid):
        iam      = aws.client('iam')
        response = iam.create_user(UserName=userid)   #aws docs say username is the only required field
        try:
            print(f'{userid} has been created successfully')
        except:
            print(f'{userid} did not complete successfully, please check your function and try again')
        return

    def create_user_accesskeys(userid):
        iam      = aws.client('iam')
        response = iam.create_access_key(UserName=userid)
        try:
            ### Display Access Keys to the terminal ####
#            print(f"Access Key ID: {response['AccessKey']['AccessKeyId']}")
#            print(f"Secret Key ID: {response['AccessKey']['SecretAccessKey']}")


        ### Write IAM Keys to file so that it is not displayed to the terminal ####
             credsfile = open('creds.txt', 'w')
             credsfile.write(f"Access Key ID: {response['AccessKey']['AccessKeyId']}\nSecret Key ID:: {response['AccessKey']['SecretAccessKey']}")
             credsfile.close()

        except:
            print(f'{userid} keys did not create successfully, please check your function and try again')
        return

    def attach_userpolicy(userid, PolicyArn):
        iam      = aws.client('iam')
        response = iam.attach_user_policy(UserName=userid,PolicyArn=ec2readonly)
        try:
            print(f'Policy has been applied to {userid} successfully')
        except:
            print(f'Policy was not applied, please check your function and try again')
        finally:
            print(f'This FUNCTION HAS COMPLETED, PLEASE VERIFY VIA AWS CONSOLE')

### VALUES THAT ARE READ FROM A CLASS LEVEL  ####
userinput   = input("Please enter the username you would like to create: ")
userid      = userinput + str(random.randint(10,99))
ec2readonly = 'arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess'

### CLASS.METHOD(PARAMETERS) - THIS SECTION ACTUALLY CALLS THE CLASS.FUNCTION WE WANT TO PRINT TO THE SCREEN/FILE ###
aws_iam.newuser(userid)
aws_iam.create_user_accesskeys(userid)
aws_iam.attach_userpolicy(userid,PolicyArn=ec2readonly)