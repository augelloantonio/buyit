from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


class TestAccountsBackend(TestCase):
    ''' Test accounts app backend.py '''

    # testing login with an email address instead of a username
    def test_login_with_email_address(self):

        username_or_email = None
        password = None

        # creates a test user
        user = User.objects.create_user(
            username='username', email='myemail@test.com', password='password')

        id = user.id

        # logs in the test user
        self.client.login(username='username',
                          email='myemail@test.com', password='password')

        # login url
        page = self.client.get("/accounts/login/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is index.html
        self.assertTemplateUsed(page, "profile.html")
        user = get_object_or_404(User, pk=id)
        self.assertEqual(user.username, 'username')

    # testing login with a correct email address and a wrong password
    def test_login_with_a_registered_email_address_and_wrong_password(self):

        # create a user to test
        user = User.objects.create_user('username',
                                        'myemail@test.com', 'password')
        # try to login the user with:
        # the correct email address
        # but the wrong password
        self.client.login(
            username_or_email='myemail@test.com', password='wrong')
        # login url
        page = self.client.get("/accounts/login/", follow=True)
        # check the status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login.html
        self.assertTemplateUsed(page, "login.html")

    # tesing login with correct details but the user is not an active user
    def test_login_with_email_address_but_inactive_user(self):

        # create an inactive user to test
        user = User.objects.create_user('username',
                                        'myemail@test.com',
                                        'password', is_active=False)
        # try to log in the inactive user
        self.client.login(
            username_or_email='myemail@test.com', password='password')
        # login url
        page = self.client.get("/accounts/login/", follow=True)
        # check status code is 200
        self.assertEqual(page.status_code, 200)
        # check Template Used is login.html
        self.assertTemplateUsed(page, "login.html")
