import unittest
from password import Password

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
    self.new_password = Password("wadi","gmail.com","@wadi123") # create contact object

def test_init(self):
    '''
    test_init_case to test if the object is being initialized properly
    '''

    self.assertEqual(self.new_password.username,"wadi")
    self.assertEqual(self.new_password.website, "gmail.com")
    self.assertEqual(self.new_password.password,"@wadi123")












def test_save_password(self):
    '''
    test_save_contact test case to test if the password object is saved to the password list
    '''
    self.new_password.save_password() #saving the new password
    self.assertEqual(len(Password.password_list),1)






























































    if __name__ ==  '__main__':
        unittest.main()