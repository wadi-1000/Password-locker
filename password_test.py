import unittest  # import unittest module
from password import Credentials  # import class Credentials
from password import User


class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """

    def test_check_user(self):
        '''
        Function to test whether the login in function check_user works as expected
        '''
        self.new_user = User('Joy', 'Zawadi', '2345')
        self.new_user.save_user()
        user2 = User('Wendy', 'Muhoho', '9857')
        user2.save_user()

        for user in User.users_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user = user.first_name
        return current_user

        self.assertEqual(current_user, Credential.check_user(
            user2.password, user2.first_name))

    def setUp(self):
        '''
        Method that runs tests before each test case has run.
        '''
        self.new_password = Credentials(
            "wadi", "gmail.com", "@wadi123")  # create password object

    def test_init(self):
        '''
        test_init_case to test if the object is being initialized properly
        '''

        self.assertEqual(self.new_password.username, "wadi")
        self.assertEqual(self.new_password.website, "gmail.com")
        self.assertEqual(self.new_password.password, "@wadi123")

    def tearDown(self):
        '''
        tearDown method that runs tests after each test case is run.
        '''
        Credentials.credentials_list = []

    def test_save_password(self):
        '''
        test_save_contact test case to test if the password object is saved to the password list
        '''
        self.new_password.save_password()  # saving the new password account
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_passwords(self):
        '''
        test_save_multiple_passwords to check if we can save multiple contacts
        '''
        self.new_password.save_password()
        test_password = Credentials(
            "wendy", "tiktok.com", "@muhoho456")  # new password account
        test_password.save_password()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_password(self):
        '''
        test_delete_password to test if a user can delete a password
        '''
        self.new_password.save_password()
        # Create a password account
        test_password = Credentials("mugata", "mugata.com", "@mugata789")
        test_password.save_password()

        self.new_password.delete_password()
        self.assertEqual(len(Credentials.credentials_list),
                         1)  # Deleting a password account

    def test_find_password_by_website(self):
        '''
        test_find_password_by_website test to find password by website in credentials_list
        '''
        self.new_password.save_password()
        test_password = Credentials("natalie", "natalie.com", "@natalie345")
        test_password.save_password()

        found_password = Credentials.find_by_website("natalie.com")
        self.assertEqual(found_password.website, test_password.website)

    def test_display_all_passwords(self):
        '''
        method that returns a list of all passwords saved
        '''

        self.assertEqual(Credentials.display_passwords(),
                         Credentials.credentials_list)

    def test_password_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the password.
        '''

        self.new_password.save_password()
        test_password = Credentials("Test","user.gmail.com","1234",) # new account
        test_password.save_password()

        password_exists = Credentials.password_exist("1234")

        self.assertTrue(password_exists)


if __name__ == '__main__':
    unittest.main()
