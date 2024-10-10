from django.db.models import Count
from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from syncora_api.permissions import IsUserOrReadOnly

# Create your views here.


class ProfileList(generics.ListAPIView):
    """
    Displays list of all profiles created. This view will be used for testing
    purposes only. Profiles can also be searched by username and name, and
    ordered by their creation date. Each profile also has a notes, events and
    tasks count to be used in the front end.
    """

    # Use annotate method to add notes, tasks and events count
    # to each profile. Code adapted from:
    # https://github.com/Code-Institute-Solutions/drf-api/blob/a7033eacc714c79df49679fbebd455e300e09d95/posts/views.py
    queryset = Profile.objects.annotate(
        notes_count=Count("notes", distinct=True),
        tasks_count=Count("tasks", distinct=True),
        events_count=Count("events", distinct=True),
    ).order_by("-created_on")
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["user__username", "user__first_name"]
    ordering_fields = ["created_on"]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Can retrieve a single instance of the Profile model, allow editing of the
    single instance and also allows deletion of the single instance.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsUserOrReadOnly]
