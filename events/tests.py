from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from .models import Event

# Create your tests here.
class EventListViewTests(APITestCase):

    def setUp(self):
        User.objects.create_user(username='mariam', password='pass')
        mariam = Profile.objects.get(id=1)
        Event.objects.create(
            owner=mariam,
            name="test event",
            date="2024-10-09",
            start_time="00:00",
            end_time="00:01",
            category="WORK",
            location="london",
        )
    
    def test_view_list_of_events(self):
        """Tests if a list of events can be retreived"""
        response = self.client.get('/events/')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('test event', response.content)


class CreateEventViewTests(APITestCase):

    def setUp(self):
        User.objects.create_user(username="mariam", password="pass")
        mariam = Profile.objects.get(id=1)
