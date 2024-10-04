from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Task
from syncora_api.permissions import IsOwnerOrReadOnly

# Create your views here.

class TaskList(generics.ListAPIView):
    """
    Displays list of tasks created.
    """

    queryset = Task.objects.all()