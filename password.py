import random
import string


global users_list 
class User:
	'''
	Class to create user accounts and save their information
	'''
	# Class Variables
	# global users_list
	users_list = []
	def __init__(self,first_name,last_name,password):
		'''
		Method to define the properties for each user object will hold.
		'''

		# instance variables
		self.first_name = first_name
		self.last_name = last_name
		self.password = password

	def save_user(self):
		'''
		Function to save a newly created user instance
		'''
		User.users_list.append(self)

		
        
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



    @classmethod
    def password_exist(cls,password):
        '''
        Method that checks if a password exists from the credentials list.
        Args:
            password: Password to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
        '''
        for credentials in cls.credentials_list:
            if credentials.password == password:
                    return True

        return False