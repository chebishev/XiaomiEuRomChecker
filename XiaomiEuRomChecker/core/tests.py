from django.test import TestCase
from .functionality import *


# Create your tests here.
class TestFunctionality(TestCase):
    pass

    def test_get_date(self):
        self.assertEqual(get_date("2022-01-01"), [2022, 1, 1])

    def test_get_date_as_string(self):
        first_string = "updated < 4 hours ago"
        second_string = "2022-01-01"
        self.assertEqual(get_date_as_string(first_string),
                         f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}")
        self.assertEqual(get_date_as_string(second_string), "2022-01-01")
