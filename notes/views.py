from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
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
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend
    ]
    search_fields = ["title", "content"]
    ordering_fields = ["date_created", "date_updated"]


class CreateNote(generics.CreateAPIView):
    """Allows user to create a new note if authorised."""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Make logged in user owner of the note"""
        profile = self.request.user.profile
        serializer.save(owner=profile)


class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    """Allow owner of the note to update and/or delete their own note.
    Otherwise, allows read-only access."""

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [IsOwnerOrReadOnly]
