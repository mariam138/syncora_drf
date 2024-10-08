from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Note

# Create your tests here.
class NoteListViewTests(APITestCase):

    def setUp(self):
        User.objects.create_user(username='mariam', password="pass")
    
    def test_view_list_of_notes(self):
        mariam = User.objects.get(username='mariam')
        Note.objects.create(owner=mariam, title='title', content='content')
        response = self.client.get('/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)