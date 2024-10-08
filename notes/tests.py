from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from profiles.models import Profile
from .models import Note


# Create your tests here.
class NoteListViewTests(APITestCase):

    def setUp(self):
        User.objects.create_user(username="mariam", password="pass")

    def test_view_list_of_notes(self):
        """Tests if a list of notes can be retrieved."""
        mariam = Profile.objects.get(id=1)
        Note.objects.create(owner=mariam, title="title", content="content")
        response = self.client.get("/notes/")
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
        self.client.login(username="mariam", password="pass")
        response = self.client.post("/notes/new/", {"content": "content"})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unauthenticated_user_cannot_create_note(self):
        """Tests if an unauthorised user is unable to create a new note"""
        response = self.client.post(
            "/notes/new/", {"title": "title", "content": "content"}
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class NoteDetailViewTests(APITestCase):

    def setUp(self):
        User.objects.create_user(username="mariam", password="pass")
        mariam = Profile.objects.get(id=1)
        Note.objects.create(owner=mariam, title="title", content="content")

        User.objects.create_user(username="fakemariam", password="pass")

    def test_user_can_retreive_note_detail(self):
        """Test user can get a note by it's id"""
        response = self.client.get("/notes/1/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_owner_can_update_own_note(self):
        """Test owner of note can update it"""
        self.client.login(username="mariam", password="pass")
        response = self.client.put("/notes/1/", {"content": "new content"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__user_cannot_update_another_users_note(self):
        """Tests that a user cannot update another user's notes"""
        self.client.login(username="fakemariam", password="pass")
        response = self.client.put("/notes/1/", {"content": "new fake content"})

        self.assertNotEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_can_delete_own_note(self):
        """Test that a user can delete their own note"""
        self.client.login(username="mariam", password="pass")
        response = self.client.delete("/notes/1/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_user_cannot_delete_another_users_note(self):
        """Test that a user cannot delete another user's note"""
        self.client.login(username="fakemariam", password="pass")
        response = self.client.delete("/notes/1/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
