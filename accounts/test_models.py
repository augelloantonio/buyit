from django.test import TestCase
from django.contrib.auth.models import User


class TestAccountsModel(TestCase):
    ''' test the account model '''

    def test_account_model(self):
        # create and save a user
        user = User.objects.create_user(username='username',
                                        email='myemail@test.com',
                                        password='!123passwOrd')
        user.save()
        # check if each field value is equal
        # to the value entered for the user
        self.assertEqual(user.username, "username")
        self.assertEqual(user.email, "myemail@test.com")