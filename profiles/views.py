from django.shortcuts import render
from rest_framework import generics
from .models import Profile
from .serializers import ProfileSerializer

# Create your views here.

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
