from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.user.username")

    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "title",
            "due_date",
            "priority",
            "category",
            "description",
            "completed",
        ]


class CreateTaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.user.username")
    completed = serializers.ReadOnlyField(source="task.completed")

    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "title",
            "due_date",
            "priority",
            "category",
            "description",
            "completed",
        ]
