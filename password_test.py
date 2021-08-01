import unittest #import unittest module
from password import Credentials #import class Credentials
from password import User

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User('JoyKiranga','12345678kls')

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username,'JoyKiranga')
        self.assertEqual(self.new_user.password,'12345678kls')

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

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
        self.new_password = Credentials("wadi","gmail.com","@wadi123") # create password object

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
        Credentials.credentials_list = []

    def test_save_password(self):
        '''
        test_save_contact test case to test if the password object is saved to the password list
        '''
        self.new_password.save_password() #saving the new password account
        self.assertEqual(len(Credentials.credentials_list),1)



    def test_save_multiple_passwords(self):
        '''
        test_save_multiple_passwords to check if we can save multiple contacts
        '''
        self.new_password.save_password()
        test_password = Credentials("wendy","tiktok.com","@muhoho456") #new password account
        test_password.save_password()
        self.assertEqual(len(Credentials.credentials_list),2)



    def test_delete_password(self):
        '''
        test_delete_password to test if a user can delete a password
        '''
        self.new_password.save_password()
        test_password = Credentials("mugata","mugata.com","@mugata789") #Create a password account
        test_password.save_password()
        
        self.new_password.delete_password()
        self.assertEqual(len(Credentials.credentials_list),1) #Deleting a password account


    def test_find_password_by_website(self):
            '''
            test_find_password_by_website test to find password by website in credentials_list
            '''
            self.new_password.save_password()
            test_password = Credentials("natalie","natalie.com","@natalie345")
            test_password.save_password()

            found_password = Credentials.find_by_website("natalie.com")
            self.assertEqual(found_password.website,test_password.website)



    def test_display_all_passwords(self):
        '''
        method that returns a list of all passwords saved
        '''

        self.assertEqual(Credentials.display_passwords(),Credentials.credentials_list)


   
if __name__ ==  '__main__':
        unittest.main()