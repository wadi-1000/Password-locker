import unittest #import unittest module
from password import Password #import class Password

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Method that runs tests before each test case has run.
        '''
        self.new_password = Password("wadi","gmail.com","@wadi123") # create password object

    def test_init(self):
        '''
        test_init_case to test if the object is being initialized properly
        '''

        self.assertEqual(self.new_password.username,"wadi")
        self.assertEqual(self.new_password.website, "gmail.com")
        self.assertEqual(self.new_password.password,"@wadi123")



    def tearDown(self):
        '''
        tearDown method that runs tests after each test case is run.
        '''
        Password.password_list = []

    def test_save_password(self):
        '''
        test_save_contact test case to test if the password object is saved to the password list
        '''
        self.new_password.save_password() #saving the new password account
        self.assertEqual(len(Password.password_list),1)



    def test_save_multiple_passwords(self):
        '''
        test_save_multiple_passwords to check if we can save multiple contacts
        '''
        self.new_password.save_password()
        test_password = Password("wendy","tiktok.com","@muhoho456") #new password account
        test_password.save_password()
        self.assertEqual(len(Password.password_list),2)



    def test_delete_password(self):
        '''
        test_delete_password to test if a user can delete a password
        '''
        self.new_password.save_password()
        test_password = Password("mugata","mugata.com","@mugata789") #Create a password account
        test_password.save_password()
        
        self.new_password.delete_password()
        self.assertEqual(len(Password.password_list),1) #Deleting a password account


if __name__ ==  '__main__':
        unittest.main()