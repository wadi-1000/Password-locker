#!/usr/bin/env python3.9
# import hashlib
# import binascii
# import os
import random
import string
from password import User
from password import Credentials


def create_user(fname, lname, password):
    '''
    Function to create a new user account
    '''
    new_user = User(fname, lname, password)
    return new_user


def save_user(user):
    '''
    Function to save a new user account
    '''
    User.save_user(user)


def verify_user(first_name, password):
    '''
    Function that verifies the existance of the user before creating credentials
    '''
    checking_user = User.check_user(first_name, password)
    return checking_user


def create_password(username, website, password):
    '''
    Function to generate a new password account
    '''

    new_password = Credentials(username, website, password)
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
    password.delete_password()


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


def find_password(website):
    '''
    Function that finds a account by website and returns the account
    '''
    return Credentials.find_by_website(website)


def check_existing_password(password):
    '''
    Function that check if a password exists with that password and return a Boolean
    '''
    return Credentials.password_exist(password)


def main():
    print("Welcome to locka the password locker of your choice")
    print("What is your name?")
    name = input("Name: ")
    print(f"Hi {name}!")
    print("Where would you like to start?")
    print('\n')
    while True:
        print(' ')
        print("-"*60)
        print(
            'Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')
        short_code = input('Enter a choice: ').lower().strip()
        if short_code == 'ex':
            break

        elif short_code == 'ca':
            print("-"*60)
            print(' ')
            print('To create a new account:')
            first_name = input('Enter your first name - ').strip()
            last_name = input('Enter your last name - ').strip()
            password = input('Enter your password - ').strip()
            save_user(create_user(first_name, last_name, password))
            print(" ")
            print(
                f'New Account Created for: {first_name} {last_name} using password: {password}')
        elif short_code == 'li':
            print("-"*60)
            print(' ')
            print('To login, enter your account details:')
            user_name = input('Enter your first name - ').strip()
            password = str(input('Enter your password - '))
            user_exists = verify_user(user_name, password)
            if user_exists == user_name:
                print(" ")
                print(
                    f'Welcome {user_name}. Please choose an option to continue.')
        while True:
            print("Use these short codes:  cp - create a new password, fp -find a password, ex -exit the password list, dp -deleting a password, sp -saving a password, dc -display passwords")
            short_code = input().lower()

            if short_code == 'cp':
                print("Generate a new password")
                print('\n')

                # username
                print("Username of website:  ")
                username = input()

                # website
                print("Website:  ")
                website = input()

                # generate random password
                length = int(input('\nEnter the length of password: '))
                lower = string.ascii_lowercase
                upper = string.ascii_uppercase
                num = string.digits
                symbols = string.punctuation

                all = lower + upper + num + symbols

                temp = random.sample(all, length)
                password = "".join(temp)

                # all = string.ascii_letters + string.digits + string.punctuation
                # pass = "".join(random.sample(all,length))

                print(f"Your new username is {username}")
                print(f"Your website is {website}")
                print(f"Your new password is {password}")
                # #hide password
                # salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii'
                # pwdhash = hashlib.pbkdf2_hmac('sha512',password.encode('utf-8'),salt, 100000)
                # pwdhash = binascii.hexlify(pwdhash)
                # new_password = (salt + pwdhash).decode('ascii')

                # to create and save new password account
                save_password(create_password(username, website, password))
                print('\n')
                print(
                    f"New Password Account {username}, {website}, {password} created")
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
                new_password = (username, website, password)
                save_password(new_password)
                print('\n')
                print(f"Saved Password: {username}, {website}, {password}")
                print('\n')

            elif short_code == 'dc':
                if display_passwords():
                    print("Here is a list of all your passwords")
                    print('\n')

                    for password in display_passwords():
                        print(
                            f"{password.username} {password.website} .....{password.password}")

                        print('\n')
                else:
                    print('\n')
                    print("You dont seem to have any passwords saved yet")
                    print('\n')

            elif short_code == 'fp':

                print("Enter the password you want to search for")

                search_password = input()
                if check_existing_password(search_password):
                    search_account = (find_password(search_password))
                    print(
                        f"{search_account.username} {search_account.website} {search_account.password}")
                    print('-' * 20)

                    print(f"Username.......{search_account.username}")
                    print(f"Website.......{search_account.website}")
                    print(f"Password.......{search_account.password}")
                else:
                    print("That password does not exist")
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

                delete_password(username, website, password)
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
