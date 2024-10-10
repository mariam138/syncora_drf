from rest_framework import generics, filters
from .models import Profile
from .serializers import ProfileSerializer
from syncora_api.permissions import IsUserOrReadOnly

# Create your views here.


class ProfileList(generics.ListAPIView):
    """
    Displays list of all profiles created. This view will be used for testing
    purposes only.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ["user__username", "user__first_name"]


class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Can retrieve a single instance of the Profile model, allow editing of the
    single instance and also allows deletion of the single instance.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsUserOrReadOnly]