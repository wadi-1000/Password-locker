import unittest
form password import Password

class TestPassword(unittest.TestCase):

    '''
    Test class that defines test cases for the password class behaviours

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def tearDown(self):
        '''
        Method that runs tests after the code has run.
        '''
        Password.password_list = []
        