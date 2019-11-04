from django.apps import apps
from django.test import TestCase
from .apps import AccountsConfig


class TestAccountsApp(TestCase):
    ''' test that 'accounts' is equal to the the config name '''

    def test_app(self):
        self.assertEqual("accounts", AccountsConfig.name)
