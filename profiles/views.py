from django.shortcuts import render
from .models import Profile
from rest_framework import generics

# Create your views here.

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()