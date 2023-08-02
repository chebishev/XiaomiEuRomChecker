from datetime import datetime

from django.test import TestCase
from .functionality import get_date, get_date_as_string


# Create your tests here.
class TestFunctionality(TestCase):
    def setUp(self) -> None:
        self.first_string = "updated < 4 hours ago"
        self.second_string = "2022-01-01"

    def test_get_date(self):
        # if it works correctly it has to convert the string into a list of integers representing the date in format:
        # [year, month, day]
        self.assertEqual(get_date(self.second_string), [2022, 1, 1])

    def test_get_date_as_string(self):
        # if the "date" is something less than 24 hours it will have "<" in the string
        # so the function must convert it to today's date
        self.assertEqual(get_date_as_string(self.first_string),
                         f"{datetime.now().year}-{datetime.now().month}-{datetime.now().day}")

        # else the function must return the input string
        self.assertEqual(get_date_as_string(self.second_string), self.second_string)
