from django.test import TestCase
from pyshorteners.exceptions import ShorteningErrorException

from .functionality import shorten_url
from .models import LinksModel
from ..auth_app.models import AuthUser


# Create your tests here.
class TestLinkShortener(TestCase):
    pass

    def test_invalid_url_shortener_with_integer(self):
        first_url = 1
        with self.assertRaises(AttributeError):
            self.assertEqual(shorten_url(first_url),
                             "'int' object has no attribute 'startswith'")

    def test_invalid_url_shortener_with_string(self):
        first_url = "atanas"
        with self.assertRaises(ShorteningErrorException):
            self.assertEqual(shorten_url(first_url),
                             'There was an error on trying to short the url: b\'{'
                             '"message":"INVALID_ARG_LONG_URL","resource":"bitlinks",'
                             '"description":"The value provided is invalid.","errors":[{'
                             '"field":"long_url","error_code":"invalid"}]}\'')
