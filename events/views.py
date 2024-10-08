from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Event
from .serializers import EventSerializer
from syncora_api.permissions import IsOwnerOrReadOnly

# Create your views here.

class EventList(generics.ListAPIView):
    """
    Displays list of events created.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer


class CreateEvent(generics.CreateAPIView):
    """
    Allows user to create new event instance.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        profile = self.request.user.profile
        serializer.save(owner=profile)
    

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieves an event using it's id. Can also allow the user to update
    and delete the event by using it's id.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]