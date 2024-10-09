from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from .models import Event


# Create your tests here.
class EventListViewTests(APITestCase):

    def setUp(self):
        User.objects.create_user(username="mariam", password="pass")
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
        response = self.client.get("/events/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("test event", response.content)


class CreateEventViewTests(APITestCase):

    def setUp(self):
        User.objects.create_user(username="mariam", password="pass")
        mariam = Profile.objects.get(id=1)

    def test_authenticated_user_can_create_new_event(self):
        """Test if a logged in user can create a new event"""
        self.client.login(username="mariam", password="pass")
        response = self.client.post(
            "/events/new/",
            {
                "owner": "mariam",
                "name": "test event",
                "date": "2024-10-09",
                "start_time": "00:00",
                "end_time": "00:01",
                "category": "WORK",
                "location": "london",
            },
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        def test_unauthorised_user_cannot_create_new_event(self):
            """Tests that a user cannot create a new event if not logged in"""
            response = self.client.post(
                "/events/new/",
                {
                    "name": "test event",
                    "date": "2024-10-09",
                    "start_time": "00:00",
                    "end_time": "00:01",
                    "category": "WORK",
                    "location": "london",
                },
            )

            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class EventDetailViewTests(APITestCase):
    """Tests associated with the EventDetail view"""

    def setUp(self):
        User.objects.create_user(username="mariam", password="pass")
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

        User.objects.create_user(username="fakemariam", password="pass")

    def test_user_can_retreieve_event_detail(self):
        """Test that any user can retreieve an event's detail"""
        response = self.client.get("/events/1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_event_owner_can_update_event(self):
        """Tests that the owner of an event can update it. Both
        put and patch requests are tested."""
        self.client.login(username="mariam", password="pass")

        response = self.client.patch("/events/1/", {"location": "dubai"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_2 = self.client.patch(
            "/events/1/",
            {
                "name": "test event",
                "date": "2024-10-09",
                "start_time": "00:00",
                "end_time": "00:01",
                "category": "WORK",
                "location": "london",
                "notes": "a note",
            },
        )

        self.assertEqual(response_2.status_code, status.HTTP_200_OK)

    def test_user_cannot_update_another_users_event(self):
        """Tests that a user cannot edit another user's event"""

        self.client.login(username="fakemariam", password="pass")

        response = self.client.patch("/events/1/", {"notes": "fakemariam notes"})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
    
    def test_owner_can_delete_event(self):
        """Tests that the owner of an event can delete the event"""
        self.client.login(username='mariam', password='pass')

        response = self.client.delete('/events/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
