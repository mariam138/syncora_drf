from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from .models import Note

# Create your tests here.
class NoteListViewTests(APITestCase):

    def setUp(self):
        User.objects.create_user(username='mariam', password="pass")

    def test_view_list_of_notes(self):
        """Tests if a list of notes can be retrieved."""
        mariam = Profile.objects.get(id=1)
        Note.objects.create(owner=mariam, title='title', content='content')
        response = self.client.get('/notes/')
        # Checks if a 200 status code is received
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Checks if the note title is on the page
        self.assertTrue(
            "title", response.content
        )  # Checks if the note content is on the page
        self.assertTrue("content", response.content)


class CreateNoteViewTests(APITestCase):

    def setUp(self):
        User.objects.create_user(username="mariam", password="pass")
    
    def test_authenticated_user_can_create_note(self):
        """Tests if an authorised user can create a new note"""
        self.client.login(username='mariam', password='pass')
        response = self.client.post('/notes/new/', {'content': 'content'})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
