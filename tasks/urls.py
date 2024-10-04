from django.urls import path
from .views import TaskList, CreateTask

urlpatterns = [
    path("tasks/", TaskList.as_view(), name="task_list"),
    path("tasks/new/", CreateTask.as_view(), name="create_task"),
]
