from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Profile


# Create your tests here.


class ProfileDetailViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(
            username="mariam", first_name="mariam", password="pass"
        )

        User.objects.create_user(
            username="fakemariam", first_name="mariam", password="pass"
        )

    def test_retreive_profile_by_id(self):
        """Tests that a profile can be retrieved by id"""
        response = self.client.get('/profiles/1')
        print(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK) 