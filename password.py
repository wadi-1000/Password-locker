import random
import string

class User:
    '''
    Class that generates and stores users passwords by creating a password account
    '''


    password_list = []


    def __init__(self,username,website,password):
        '''
        Function that dicates data gotten from user input


        Args:
            username: username.
            website: website.
            password: password.
        '''

        self.username = username
        self.website = website
        self.password = password

    def save_password(self):
        '''
        store_password method saves new passwords after generating them for a website stated by the user
        '''

        User.password_list.append(self)

    def delete_password(self):
        '''
        method that deletes a password account from password_list
        '''
        User.password_list.remove(self)


    @classmethod
    def find_by_website(cls,website):
        '''
        Method that takes in a number and returns a password that matches that website.

        Args:
            website: Website to search for
        Returns:
            Password of account that matches the number.
        '''

        for password in cls.password_list:
            if pa.website == website:
                return password

