from django.test import TestCase

from app.calc import add

class CalcTest(TestCase):

    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(add(3, 8), 11)

#docker-compose run app sh -c "python manage.py test"