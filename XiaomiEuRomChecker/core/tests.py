from datetime import datetime

from django.test import TestCase
from django.urls import reverse

from .functionality import get_date, get_date_as_string
from .views import index


# Create your tests here.
class TestFunctionality(TestCase):
    def setUp(self) -> None:
        self.first_string = "<"
        self.second_string = "2022-01-01"

    def test_get_date(self):
        # if it works correctly it has to convert the string into a list of integers representing the date in format:
        # [year, month, day]
        # there is no case that anything different from yyyy-mm-dd will be passed
        self.assertEqual(get_date(self.second_string), [2022, 1, 1])

    def test_get_date_as_string(self):
        # if the "date" is something less than 24 hours it will have "<" in the string
        # so the function must convert it to today's date
        self.assertEqual(get_date_as_string(self.first_string),
                         f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}")

        # else the function must return the input string
        self.assertEqual(get_date_as_string(self.second_string),
                         self.second_string)


class TestViews(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('localhost:8000')
        self.assertEqual(response.status_code, 302)
