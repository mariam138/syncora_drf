from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Note
from .serializers import NoteSerializer
from syncora_api.permissions import IsOwnerOrReadOnly


# Create your views here.
class NoteList(generics.ListAPIView):
    """
    Displays a list of notes to the user Notes can be searched by
    their title or their content. Notes can also be ordered by either
    their creation date or date updated, both in ascending and
    descending order.
    """

    serializer_class = NoteSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["title", "content"]
    ordering_fields = ["date_created", "date_updated"]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            owner = self.request.user.profile
            queryset = Note.objects.filter(owner=owner)
        else:
            queryset = Note.objects.all()
        return queryset


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
