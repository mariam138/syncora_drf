from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    # many=True indicates many profiles will be serialised
    serializer_class = ProfileSerializer(queryset, many=True)
