from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.user.username")
    """
    Display human readable label for category choices. This is used for the
    front end display. Code adapted from
    https://github.com/encode/django-rest-framework/issues/1755#issuecomment-945167944
    and the comment below it.
    """
    category_display = serializers.CharField(source="get_category_display", read_only=True)

    class Meta:
        model = Task
        fields = [
            "id",
            "owner",
            "title",
            "due_date",
            "priority",
            "category",
            "category_display",
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
