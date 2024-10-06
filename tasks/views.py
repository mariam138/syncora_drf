from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Task
from .serializers import TaskSerializer
from syncora_api.permissions import IsOwnerOrReadOnly

# Create your views here.

class TaskList(generics.ListAPIView):
    """
    Displays list of tasks created.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class CreateTask(generics.CreateAPIView):
    """
    Allows creation of a new task
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Get profile instance related to current user
        # .profile provided by django w/ a lowercase name of the model
        profile = self.request.user.profile
        # use the profile instance to save the task
        serializer.save(owner=profile)