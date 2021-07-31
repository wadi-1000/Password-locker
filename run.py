#!/usr/bin/env python3.9

from password import Password

def create_password(username,website,password):
    '''
    Function to generate a new password
    '''

    new_password = Password(username,website,password)
    return new_password

def save_password(password):
    '''
    Method to save a password
    '''
    password.save_password()





def main():
    print("Welcome to locka the password locker of your choice")
    name = input()
    print(input("What is your name?"))
    print(f"Hi {name}!")
    print("Where would you like to start?")
    print('\n')

    while True:
        print("Use these short codes: cp - create a new password, fp -find a password, ex -exit the password list, dp -deleting a password")

        if short_code == 'cp':
            print("Generate a new password")
            print('\n')

            #username
            username = print(str(input("Username:  ")))

            #website
            website = print(str(input("Website:  ")))

            #generate random password
            digit = print(int(input("How many digits do you want?(integers only)")))
            password = ""
            for i in range(digit):
            char = random.choice(str.ascii_letters)
            password += char

            #hide password
            


























if __name__ = "__main__"
    main()