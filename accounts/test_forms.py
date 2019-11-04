from django.test import TestCase
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth.models import User


class Test_Customer_Registration_Form(TestCase):
    ''' Test the customer registration form '''

    def test_a_valid_registration(self):
        ''' test registration form '''

        form = UserRegistrationForm({'email': 'test@gmail.com',
                                     'username': 'test',
                                     'password1': '!Testpassword2',
                                     'password2': '!Testpassword2', })
        self.assertTrue(form.is_valid())

    def test_an_invalid_registration_leaving_out_email_address(self):
        ''' test registration form is invalid
            when the email address is omitted '''

        form = UserRegistrationForm({'username': 'test',
                                     'password1': 'test',
                                     'password2': 'test', })
        self.assertFalse(form.is_valid())

    def test_an_invalid_registration_leaving_out_username(self):
        ''' test a registration form is
            invalid when username is omitted '''

        form = UserRegistrationForm({'email': 'test@gmail.com',
                                     'password1': 'test',
                                     'password2': 'test', })
        self.assertFalse(form.is_valid())

    def test_an_invalid_registration_leaving_out_password1(self):
        ''' test registration form is
            invalid if password 1 is omitted '''

        form = UserRegistrationForm({'email': 'test@gmail.com',
                                     'username': 'test',
                                     'password2': 'test', })
        self.assertFalse(form.is_valid())

    def test_an_invalid_registration_leaving_out_password2(self):
        ''' test registration form is invalid if password 2 is omitted '''

        form = UserRegistrationForm({'email': 'test@gmail.com',
                                     'username': 'test',
                                     'password1': 'test', })
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_username(self):
        ''' Test if the username is not inputted
            the message 'This field is
            required.' is shown '''

        form = UserRegistrationForm({'username': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], [u'This field is required.'])

    def test_correct_message_for_missing_password1(self):
        ''' Test if the password1 is not inputted
            the message 'This field is
            required.' is shown '''

        form = UserRegistrationForm({'password1': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password1'],
                         [u'This field is required.'])

    def test_correct_message_for_missing_password2(self):
        ''' Test if the password2 is not inputted
            the message 'This field is
            required.' is shown '''

        form = UserRegistrationForm({'password2': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'],
                         [u'This field is required.'])

    def test_correct_message_for_invalid_email(self):
        ''' Test if the email address does not
            contain @ and . that the message
            'Enter a valid email address.' is shown '''

        form = UserRegistrationForm(
            {'email': 'test with invalid email syntax'})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['email'],
                         [u'Enter a valid email address.'])

    def test_when_email_address_is_already_associated_with_another_user(self):
        ''' Test if the inputted email address
            is the same as another users email address
            the message 'Email addresses must be unique'''

        user = User.objects.create_user(username='user',
                                        email='myemail@test.com',
                                        password='password')
        user2 = {'username': 'username',
                 'email': 'myemail@test.com',
                 'password': 'password'}
        form = UserRegistrationForm(user2)
        self.assertEqual(form.errors['email'],
                         [u'Email addresses must be unique.'])

    def test_a_invalid_registration_with_different_passwords(self):
        ''' Test that if two passwords inputted
        are not the same the message 'Passwords do not match' is shown '''

        form = UserRegistrationForm({'email': 'test@gmail.com',
                                     'username': 'test',
                                     'password1': 'test',
                                     'password2': 'wrong', })
        self.assertEqual(form.errors['password2'],
                         [u'Passwords do not match'])


class Test_Login_Form(TestCase):
    ''' Test the login form '''

    def test_a_valid_login_form(self):
        ''' Test that the login form returns valid with valid input '''

        form = UserLoginForm(
            {'username_or_email': 'test', 'password': 'test', })
        self.assertTrue(form.is_valid())

    def test_an_invalid_login_form_with_no_username_input(self):
        ''' Test that the login form return invalid
        with no username inputted '''

        form = UserLoginForm({'username_or_email': '', 'password': 'test', })
        self.assertFalse(form.is_valid())

    def test_an_invalid_login_form_with_no_password_input(self):
        ''' Test that the login form return invalid
        with no password inputted '''

        form = UserLoginForm({'username_or_email': 'test', 'password': '', })
        self.assertFalse(form.is_valid())

    def test_correct_message_for_missing_username(self):
        ''' Test that the form error
        'This field is required' occurs
        when the username is missing '''

        form = UserLoginForm({'username_or_email': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username_or_email'], [u'This field is required.'])

    def test_correct_message_for_missing_password(self):
        ''' Test that the form error 'This field is
        required' occurs when the password is missing '''

        form = UserLoginForm({'password': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password'], [u'This field is required.'])
