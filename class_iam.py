import boto3 as aws
import random
from cryptography.fernet import Fernet


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
    

    def write_key():
    #Generates a key and save it into a file
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

        return

    def load_key():
    #Loads the key from the current directory named `key.key`
        return open("key.key", "rb").read()

    # Create key for file encryption of credentials
    def encrypt(filename, key):
    # Given a filename (str) and key (bytes), it encrypts the file and write it
        f = Fernet(key)

        with open('creds.txt', "rb") as file:
            # read all file data
            file_data = file.read()
        
        # encrypt data
        encrypted_data = f.encrypt(file_data)
            # write the encrypted file
        with open('creds.txt', "wb") as encrypted_file:
            encrypted_file.write(encrypted_data)
        return open('creds.txt', 'rb').read()


    def decrypt(filename, key):
    # Given a filename (str) and key (bytes), it decrypts the file and write it
        f = Fernet(key)
        with open('creds.txt', "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
        # decrypt data
        decrypted_data = f.decrypt(encrypted_data)
        # write the original file
        with open('creds.txt', "wb") as file:
            file.write(decrypted_data)

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
# uncomment this if it's the first time you run the code, to generate the key
# if you are running this to decrypt the key file, comment out the write_key(), and any aws_iam.encrypt() & uncomment out the aws_iam.decrypt()
aws_iam.write_key()
# load the key
key = aws_iam.load_key()
# file name
file = "creds.txt"

# Now, create all the good stuff....
# comment decryption out on first run
# after first run, comment out all other functions below to decrypt the creds.txt file
aws_iam.newuser(userid)
aws_iam.attach_userpolicy(userid,PolicyArn=ec2readonly)
aws_iam.create_user_accesskeys(userid)
# encrypt the creds.txt
aws_iam.encrypt(file, key)

# uncomment below after first run to descrypt the creds.txt
#aws_iam.decrypt(file,key)

# Bryant Witcher - December 26, 2021