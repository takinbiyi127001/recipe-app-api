from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """Test Cases for users"""
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@yahoo.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalised(self):
        """Test the email for a new user is normalized"""
        email = 'test@YAHOO.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(email=None,
            password='test123')

    def test_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@yahoo.com',
            password='test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
