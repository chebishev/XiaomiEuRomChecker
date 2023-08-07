from django.contrib.auth import get_user_model
from django.test import TestCase

UserModel = get_user_model()


class UserModelTest(TestCase):
    def test_user_creation(self):
        auth_user = UserModel.objects.create(username='atanas', password='naskoparola456', preferred_device='POCO F3')

        # Check that the AuthUser is created with the correct username and preferred_device
        self.assertEqual(auth_user.username, 'atanas')
        self.assertEqual(auth_user.preferred_device, 'POCO F3')

    def test_authuser_str_representation(self):
        auth_user = UserModel.objects.create(username='atanas', password='naskoparola456', preferred_device='No Device')

        # Check that the __str__ method returns the expected string representation
        expected_str = 'atanas'
        self.assertEqual(str(auth_user), expected_str)

    def test_user_model_deletion(self):
        profile = UserModel.objects.create(username='atanas', password='naskoparola456')
        profile.delete()

        # Check that the profile is deleted
        self.assertFalse(UserModel.objects.filter(pk=profile.pk).exists())
