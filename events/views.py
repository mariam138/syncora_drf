from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Event
from .serializers import EventSerializer
from syncora_api.permissions import IsOwnerOrReadOnly

# Create your views here.


class EventList(generics.ListAPIView):
    """
    Displays list of events created. Events can be searched for
    in the API by the event name. Events can also be ordered by their
    date in either ascending or descending order. Filtering by
    the event model's fields is also allowed with the owner, category
    and location fields.
    """

    # queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["name"]
    ordering_fields = ["date"]
    filterset_fields = ["owner", "category", "location"]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            owner = self.request.user.profile
            queryset = Event.objects.filter(owner=owner)
        else:
            queryset = Event.objects.all()
        return queryset


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
