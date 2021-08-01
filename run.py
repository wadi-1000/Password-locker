#!/usr/bin/env python3.9
# import hashlib
# import binascii
# import os
import random
import string
from credentials import Credentials

def create_password(username,website,password):
    '''
    Function to generate a new password account
    '''

    new_password = Credentials(username,website,password)
    return new_password

def save_password(password):
    '''
    Method to save a password account
    '''
    password.save_password()

def delete_password(password):
    '''
    Function to delete a password account
    '''
    credentials.delete_password()

def find_by_website(website):
    '''
    Function that finds a password account by a website
    '''
    return Credentials.find_by_website(website)

def display_passwords():
    '''
    Function that returns all saved passwords
    '''
    return Credentials.display_passwords()




def main():
    print("Welcome to locka the password locker of your choice")
    print("What is your name?")
    name = input("Name: ")
    print(f"Hi {name}!")
    print("Where would you like to start?")
    print('\n')

    while True:
        print("Use these short codes: cp - create a new password, fp -find a password, ex -exit the password list, dp -deleting a password, sp -saving a password, dc -display passwords")
        short_code = input().lower()
        if short_code == 'cp':
            print("Generate a new password")
            print('\n')

            #username
            print("Username:  ")
            username = input()

            #website
            print("Website:  ")
            website = input()

            #generate random password
            length = int(input('\nEnter the length of password: '))
            lower = string.ascii_lowercase
            upper = string.ascii_uppercase
            num = string.digits
            symbols = string.punctuation

            all = lower + upper + num + symbols

            temp = random.sample(all,length)
            password = "".join(temp)

            # all = string.ascii_letters + string.digits + string.punctuation
            # pass = "".join(random.sample(all,length))

            print(f"Your new username is {username}")
            print(f"Your new website is {website}")
            print(f"Your new password is {password}")
            # #hide password
            # salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii'
            # pwdhash = hashlib.pbkdf2_hmac('sha512',password.encode('utf-8'),salt, 100000)
            # pwdhash = binascii.hexlify(pwdhash)
            # new_password = (salt + pwdhash).decode('ascii')


            save_password(create_password(username,website,password)) #to create and save new password account
            print('\n')
            print(f"New Password Account {username}, {website}, {password} created")
            print('\n')

        elif short_code == 'sp':
            print("Save a password")
            print('\n')
            print("Username")
            username = input()

            print("Website")
            website = input()

            print("Password")
            password = input()
            new_password = (username,website,password)
            save_password(new_password)
            print('\n')
            print(f"Saved Password: {username}, {website}, {password}")
            print('\n')

        elif short_code == 'dc':
                if display_passwords():
                        print("Here is a list of all your passwords")
                        print('\n')

                        for credentials in display_passwords():
                            print(f"{credentials.username} {credentials.website} .....{credentials.password}")

                            print('\n')
                else:
                            print('\n')
                            print("You dont seem to have any passwords saved yet")
                            print('\n')

        elif short_code == 'fp':

            print("Enter the password you want to search for")

            search_password = input()
            if check_existing_password(search_password):
                    search_account = (find_contact(search_password))
                    print(f"{search_account.username} {search_account.website} {search_account.password}")
                    print('-' * 20)

                    print(f"Username.......{search_account.username}")
                    print(f"Website.......{search_account.website}")
                    print(f"Password.......{search_account.password}")
            else:
                    print("That account does not exist")
                    print('\n')
        
        elif short_code == 'dp':
            print("Delete a password")
            print('\n')
            print("Username")
            username = input()

            print("Website")
            website = input()

            print("Password")
            password = input()

            delete_password(username,website,password)
            print('\n')
            print(f"Deleted Password: {username}, {website}, {password}")
            print('\n')

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")



if __name__ == '__main__':
    main()