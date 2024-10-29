from django.test import TestCase
from .models import Corporation

#Create a test case to verify the Corporation and User models
class CorporationModelTest(TestCase):
    def test_create_corporation(self):
        Corporation.objects.create(name="Haneen Hamchou", address="Von-Merklin Str")
        self.assertEqual(Corporation.objects.count(), 1)