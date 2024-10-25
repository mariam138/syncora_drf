from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Task
from .serializers import TaskSerializer, CreateTaskSerializer
from syncora_api.permissions import IsOwnerOrReadOnly

# Create your views here.


class TaskList(generics.ListAPIView):
    """
    Displays list of tasks created. Tasks can be searched by title and
    description. Tasks can be ordered by due date and priority. Tasks
    can be filtered by the owner, priority, category and whether they have
    been completed or not. When logged in, only the user's tasks
    are displayed to them.
    """

    serializer_class = TaskSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["title", "description"]
    ordering_fields = ["due_date", "priority"]
    filterset_fields = ["owner", "priority", "category", "completed"]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            owner = self.request.user.profile
            queryset = Task.objects.filter(owner=owner)
        else:
            queryset = Task.objects.all()
        return queryset


class CreateTask(generics.CreateAPIView):
    """
    Allows creation of a new task
    """

    queryset = Task.objects.all()
    serializer_class = CreateTaskSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Get profile instance related to current user
        # .profile provided by django w/ a lowercase name of the model
        profile = self.request.user.profile
        # use the profile instance to save the task
        serializer.save(owner=profile)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Will retrieve a task by id and allow it to be viewed in detail.
    Will also allow editing and deletion of the task from one API
    end point.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOrReadOnly]
