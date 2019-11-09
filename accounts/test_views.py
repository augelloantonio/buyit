from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.messages import get_messages


class TestAccountViewsRegister(TestCase):
    ''' test register view '''

    def test_get_register_customer_page(self):
        ''' test the url returns register.html
            with a status 200 '''

        # url to register a customer
        page = self.client.get("/accounts/register/")
        # check for status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is registraion.html page
        self.assertTemplateUsed(page, "register.html")

    def test_registering_a_new_user_with_valid_form_input(self):
        ''' test registering a user with valid input '''

        # post input to the register url
        page = self.client.post('/accounts/register/',
                                {'email': 'test@email.com',
                                 'username': 'test',
                                 'password1': '!123Password',
                                 'password2': '!123Password'},
                                follow=True)
        # check for a status 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html page
        self.assertTemplateUsed(page, "profile.html")
        # check theat the stored message is
        # equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'You have successfully registered, an email has been sent to you.')

    def test_registering_a_new_user_with_incorrect_form_input(self):
        ''' test registering a user with incorrect input '''

        # post an invalid form with no password2 inputted
        page = self.client.post('/accounts/register/',
                                {'email': 'test@email.com',
                                 'username': 'test',
                                 'password1': 'password',
                                 'password2': 'password2'},
                                follow=True)
        # check for status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is register.html
        self.assertTemplateUsed(page, "register.html")

    def test_registering_a_new_user_with_valid_form_input(self):
        ''' test registering a user with valid input '''

        # post input to the register url
        page = self.client.post('/accounts/register/',
                                {'email': 'test@email.com',
                                 'username': 'test',
                                 'password1': '!123Password',
                                 'password2': '!123Password'},
                                follow=True)
        # check for a status 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html page
        self.assertTemplateUsed(page, "profile.html")
        # check theat the stored message is
        # equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'You have successfully registered, an email has been sent to you.')

    def test_registering_a_new_user_with_invalid_form_input(self):
        ''' test registering a user with invalid input '''

        # post an invalid form with no password2 inputted
        page = self.client.post('/accounts/register/',
                                {'email': 'test@email.com',
                                 'username': 'test',
                                 'password1': 'password',
                                 'password2': ''},
                                follow=True)
        # check for status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is register.html
        self.assertTemplateUsed(page, "register.html")

    def test_redirecting_user_to_personal_page_if_already_logged(self):
        # create a user
        user = User.objects.create_user('username',
                                        'myemail@test.com',
                                        'password')
        # login the user
        self.client.login(username='username',
                          password='password')

        # register url
        page = self.client.get("/accounts/register/", follow=True)
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is index.html page
        self.assertTemplateUsed(page, "profile.html")


class TestAccountViewsLogin(TestCase):
    ''' test the login view '''

    TestCase.maxDiff = None

    def test_get_login_customer_page(self):
        ''' test login url directs to login.html '''
        # url to login
        page = self.client.get("/accounts/login/")
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login.html
        self.assertTemplateUsed(page, "login.html")

    def test_login_view_when_someone_logged_in(self):
        ''' test trying to login when someone is already logged in '''

        # create a user
        user = User.objects.create_user('username',
                                        'test@test.com',
                                        'password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # url to login
        page = self.client.get("/accounts/login/", follow=True)
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html
        self.assertTemplateUsed(page, "profile.html")

    def test_login_user_with_valid_form_input(self):
        ''' test login when you input valid information '''

        # create a user
        user = User.objects.create_user('user',
                                        'myemail@test.com',
                                        '!123Password')
        # post login input to the login url
        page = self.client.post('/accounts/login/',
                                {'username_or_email': 'user',
                                 'password': '!123Password'},
                                follow=True)
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html
        self.assertTemplateUsed(page, "profile.html")
        # check the message stored is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'You have successfully logged in')

    def test_login_user_with_invalid_form_input(self):
        ''' test login with invalid form '''

        # create a user
        user = User.objects.create_user('user',
                                        'myemail@test.com',
                                        '!123Password')
        # login with the wrong password
        page = self.client.post('/accounts/login/',
                                {'username_or_email': '',
                                 'password': 'xxx'},
                                follow=True)
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login.html page
        self.assertTemplateUsed(page, "login.html")

    def test_login_user_with_wrong_form_input(self):
        ''' test login with invalid information '''

        # create a user
        user = User.objects.create_user('user',
                                        'myemail@test.com',
                                        '!123Password')
        # login with the wrong password
        page = self.client.post('/accounts/login/',
                                {'username_or_email': 'user',
                                 'password': 'xxx'},
                                follow=True)
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login.html page
        self.assertTemplateUsed(page, "login.html")


class TestAccountViewsLogout(TestCase):
    ''' test the logout view '''

    def test_get_logout_customer_page_when_someone_logged_in(self):
        ''' test logout when someone is logged in '''

        # create a user
        user = User.objects.create_user('username',
                                        'myemail@test.com',
                                        'password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # logout url
        page = self.client.get("/accounts/logout/", follow=True)
        # check for a status code 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is index.html page
        self.assertTemplateUsed(page, "index.html")
        # check the message stored is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'You have successfully logged out')

    def test_logout_customer_view_when_no_one_logged_in(self):
        ''' test the logout view when there is no one logged in '''

        # logout url
        page = self.client.get("/accounts/logout/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check template used is login page
        self.assertTemplateUsed(page, "index.html")


class TestEditAccountViewsProfile(TestCase):
    ''' test the edit profile views '''

    def test_get_profile_page_when_someone_logged_in(self):
        ''' test profile view when someone is logged in '''

        # create a user
        user = User.objects.create_user('username',
                                        'myemail@test.com',
                                        'password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # profile url
        page = self.client.get("/accounts/profile/", follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html page
        self.assertTemplateUsed(page, "profile.html")

    def test_profile_view_when_no_one_logged_in(self):
        ''' test profile view when no-one is logged in '''

        # profile url
        page = self.client.get("/accounts/profile/", follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login.html page
        self.assertTemplateUsed(page, "login.html")

    def test_edit_profile_with_valid_ammendments(self):
        ''' test editing the profile with valid ammendments '''

        # create a user
        user = User.objects.create_user('username',
                                        'test@test.com',
                                        'password')
        # login user
        self.client.login(username='username',
                          password='password')
        # edit profile url
        page = self.client.post("/accounts/editprofile/",
                                {'username': 'new',
                                 'email': 'newemail@test.com',
                                 'user': 'user'},
                                follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html page
        self.assertTemplateUsed(page, "profile.html")

    def test_edit_profile_with_invalid_form(self):
        ''' test editing the profile with invalid form '''

        # create a user
        user = User.objects.create_user('username',
                                        'test@test.com',
                                        'password')
        # login user
        self.client.login(username='username',
                          password='password')
        # edit profile url
        page = self.client.post("/accounts/editprofile/",
                                {'username': '',
                                 'email': 'newemail@test.com',
                                 'user': ''},
                                follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html page
        self.assertTemplateUsed(page, "editprofile.html")

    def test_edit_profile_to_email_address_already_in_use(self):
        ''' test editing the profile with an
            email address already in use by
            another user '''

        # create a user
        user = User.objects.create_user('username',
                                        'test@test.com',
                                        'password')
        # create a second user
        user2 = User.objects.create_user('new',
                                         'newemail@test.com',
                                         'password')
        # login the first user
        self.client.login(username='username',
                          password='password')
        # post edit profile form details to the edit profile url
        page = self.client.post("/accounts/editprofile/",
                                {'username': 'username',
                                 'email': 'newemail@test.com',
                                 'user': 'user'},
                                follow=True)
        # check Template Used is editprofile.html page
        self.assertTemplateUsed(page, "editprofile.html")
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the message stored
        # is equal to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Somebody with this email '
                         'address is already registered '
                         'please enter a unique email address')

    def test_edit_profile_when_username_is_in_use(self):
        ''' test editing the profile to a username
            that is already in use '''

        # create a user
        user = User.objects.create_user('username',
                                        'myemail@test.com',
                                        'password')
        # create a second user
        user2 = User.objects.create_user('change',
                                         'change@change.com',
                                         'password')
        # login user
        self.client.login(username='username',
                          password='password')
        # try to edit user1 username to same as user2
        page = self.client.post("/accounts/editprofile/",
                                {'username': 'change',
                                 'email': 'myemail@test.com',
                                 'user': 'user'},
                                follow=True)
        # check Template Used is editprofile.html page
        self.assertTemplateUsed(page, "editprofile.html")
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check the message stored is equal
        # to the expected message
        messages = list(get_messages(page.wsgi_request))
        self.assertEqual(str(messages[0]),
                         'Somebody already has this '
                         'username please enter a '
                         'unique username')


class TestEditUserPasswordViews(TestCase):
    ''' test the edit password views '''

    def test_get_change_password_page_when_someone_logged_in(self):
        ''' test profile view when someone is logged in '''

        # create a user
        user = User.objects.create_user('username',
                                        'myemail@test.com',
                                        'password')
        # login the user
        self.client.login(username='username',
                          password='password')
        # profile url
        page = self.client.get("/accounts/password/", follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html page
        self.assertTemplateUsed(page, "editpassword.html")

    def test_change_password_page_when_no_one_logged_in(self):
        ''' test change password view when no-one is logged in '''

        # profile url
        page = self.client.get("/accounts/password/", follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login.html page
        self.assertTemplateUsed(page, "login.html")

    def test_post_change_password_with_valid_form(self):
        ''' test edit password post with valid form '''

        # create a user
        user = User.objects.create_user('username',
                                        'myemail@test.com',
                                        '!123Password')
        # login the user
        self.client.login(username='username',
                          password='!123Password')

        # profile url
        page = self.client.post("/accounts/password/",
                                {'old_password': '!123Password',
                                 'new_password1': '!123NewPassword',
                                 'new_password2': '!123NewPassword'},
                                follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html page
        self.assertTemplateUsed(page, "profile.html")

    def test_post_change_password_with_invalid_form(self):
        ''' test edit password post with invalid form '''

        # create a user
        user = User.objects.create_user('username',
                                        'myemail@test.com',
                                        '!123Password')
        # login the user
        self.client.login(username='username',
                          password='!123Password')

        # profile url
        page = self.client.post("/accounts/password/",
                                {'old_password': '!123Password',
                                 'new_password1': '!123NewPassword',
                                 'new_password2': '123Password'},
                                follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is profile.html page
        self.assertTemplateUsed(page, "editpassword.html")
