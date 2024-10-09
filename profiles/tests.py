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

    def test_retrieve_profile_by_id(self):
        """Tests that a profile can be retrieved by id"""
        response = self.client.get("/profiles/1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cannot_retrieve_profile_that_doesnt_exist(self):
        """Tests that a user cannot retrieve a profile that has not been created"""
        response = self.client.get("/profiles/2410/")

        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
