from random import randint  
import boto3 



def username():
    print("This python program generates unique usernames.\n")

    # get the user's first and last names
    first = input("Please enter your first name (all lowercase): ")
    last = input("Please enter your last name (all lowercase): ")
    
    # concatenate first initial with 7 chars of the last name.
    uname = first[0] + last[:7]
    

    # output the username
    print("Your username is:", uname + str(randint(1, 100)))
username()