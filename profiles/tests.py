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
