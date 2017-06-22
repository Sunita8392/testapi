from django.test import TestCase
from .models import Stu
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class ModelTestCase(TestCase):
    def setUp(self):
        """Define the test client and other test variables."""
        self.Stu_roll_no=Stu(roll_no=self.Stu_roll_no)
        self.Stu_name = Stu(name=self.Stu_name)
        self.Stu_address = Stu(address=self.Stu_address)

    def test_model_can_create_stu(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Stu.objects.count()
        self.Stu.save()
        new_count = Stu.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):

        self.client = APIClient()
        self.bucketlist_data = {'name': 'Go to Ibiza'}
        self.response = self.client.post(
            reverse('create'),
            self.bucketlist_data,
            format="json")

    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)