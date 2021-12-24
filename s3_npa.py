import boto3 as aws
import pprint

region=""

def print_menu():       ## Your menu design here
    print (30 * "-" , "MENU" , 30 * "-")
    use1 = print (f"1. us-east-1")
    use2 = print (f"2. us-east-2")
    usw1 = print (f"3. us-west-1")
    usw2 = print (f"4. us-west-2")
    exit = print(f"5. EXIT")
    print (67 * "-")
  
loop=True      
  
while loop:          ## While loop which will keep going until loop = False
    print_menu()    ## Displays menu
    choice = input("Enter your choice [1-5]: ")
    choice = int(choice)
     
    if choice==1:     
        choice1 = print (f"us-east-1 has been selected")
        region = 'us-east-1'
    elif choice==2:
        choice2 = print (f"us-east-2 has been selected")
        region = 'us-east-2'
    elif choice==3:
        choice3 = print (f"us-west-1 has been selected")
        region = 'us-west-1'
    elif choice==4:
        choice4 = print (f"us-west-2 has been selected")
        region = 'us-west-2'
    elif choice==5:
        print (f"YOU WILL NOW EXIT THE MENU")
        ## You can add your code or functions here
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        input("Wrong option selection. Enter any key to try again..")

    break

def lists3_buckets():
    session = aws.Session(region_name=region)
    s3client = session.client('s3')
    bucket_list = s3client.list_buckets()
    #print(bucket_list['Buckets'])
    for bucket in bucket_list['Buckets']:
        print(f"Below is the list of buckets in {region}\nThe bucket name is: {bucket['Name']}, bucket creationdate is: {bucket['CreationDate']}\n")
        print(100 * "-")
    return
        

def get_s3_pa():
    session = aws.Session(region_name=region)
    s3client = aws.client('s3')
    bucket_name = input(f'Which bucket would you like info on ? -- **** IT MUST BE AN EXACT MATCH, SUGGEST COPY & PASTE ***:  ')
    gpa = s3client.get_public_access_block(Bucket=bucket_name, ExpectedBucketOwner='<AWS ACCOUNT#>')
        #print(f"The bucket name is: {bucket['Name']}, bucket creationdate is: {bucket['CreationDate']}")
    print(f'\nThe public access policy info for {bucket_name} \n')    
    pprint.pprint(gpa['PublicAccessBlockConfiguration'])


lists3_buckets()
get_s3_pa()


#response = s3client.delete_public_access_block(Bucket='string', ExpectedBucketOwner='string')