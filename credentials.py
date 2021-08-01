import random
import string

class User:
    """
    Create User class that generates new instances of a user.
    """
    user_list = []

    def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password

    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        User.user_list.append(self)
    

    @classmethod
    def display_user(cls):
        return cls.user_list

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)


        
class Credentials:
    '''
    Class that generates and stores users passwords by creating a password account
    '''


    credentials_list = []


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

        Credentials.credentials_list.append(self)

    def delete_password(self):
        '''
        method that deletes a password account from credentials_list
        '''
        Credentials.credentials_list.remove(self)


    @classmethod
    def find_by_website(cls,website):
        '''
        Method that takes in a number and returns a password that matches that website.

        Args:
            website: Website to search for
        Returns:
            Password of account that matches the website.
        '''

        for credentials in cls.credentials_list:
            if credentials.website == website:
                return credentials

    @classmethod
    def display_passwords(cls):
        '''
        method that returns the password list
        '''
        return cls.credentials_list



   