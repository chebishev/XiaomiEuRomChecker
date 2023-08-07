from datetime import datetime
from django.test import TestCase
from .functionality import get_date, get_date_as_string
from .models import FoldersModel


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


class TestIndexView(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('localhost:8000')
        self.assertEqual(response.status_code, 302)


class FoldersModelTest(TestCase):

    def test_model_creation(self):
        folder = FoldersModel.objects.create(
            folder_name='V14.0.23.8.1',
            last_modification_date='2023-08-01',
        )

        # Check that the folder was created with the correct fields
        self.assertEqual(folder.folder_name, 'V14.0.23.8.1')
        self.assertEqual(str(folder.last_modification_date), '2023-08-01')

    def test_model_str_representation(self):
        folder = FoldersModel.objects.create(
            folder_name='V14.0.23.8.2',
            last_modification_date='2023-08-02',
        )

        # Check that the __str__ method returns the expected string representation
        expected_str = 'V14.0.23.8.2'
        self.assertEqual(str(folder), expected_str)

    def test_unique_folder_name(self):
        # Create a folder with a specific folder_name
        FoldersModel.objects.create(
            folder_name='V14.0.23.8.3',
            last_modification_date='2023-08-03',
        )

        # Attempt to create another folder with the same folder_name
        with self.assertRaises(Exception) as context:
            FoldersModel.objects.create(
                folder_name='V14.0.23.8.3',
                last_modification_date='2023-08-04',
            )
