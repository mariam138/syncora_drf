from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.


class ProfileList(generics.ListAPIView):
    """
    Displays list of all profiles created. This view will be used for testing
    purposes only.
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
