import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from .models import Profile
from .serializers import ProfileSerializer

client = Client()

# Create your tests here.

class GetAllUsersTest(TestCase):
    """ get list of all profiles in API"""

    def setUp(self):
        self.request_user = User.objects.create_user(
            username="request_user",
            email="request_user@email.com",
            password="testpass",
            first_name="RequestUser",
        )

        # Create another user for the profile
        self.other_user = User.objects.create_user(
            username="test",
            email="test@email.com",
            password="testpass",
            first_name="user",
        )

        # Profile.objects.get_or_create(user=self.user)

        self.factory = APIRequestFactory()  # Create an instance of APIRequestFactory

    def test_get_all_users(self):
        response = self.client.get(reverse('profiles_list'))
        request = self.factory.get(reverse("profiles_list"))
        request.user = self.request_user
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(
            profiles, many=True, context={"request": request}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
