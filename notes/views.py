from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Note
from .serializers import NoteSerializer
from syncora_api.permissions import IsOwnerOrReadOnly

# Create your views here.
class NoteList(generics.ListAPIView):
    """
    Displays a list of notes to the user.
    """

    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class CreateNote(generics.CreateAPIView):
    """Allows user to create a new note if authorised."""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]