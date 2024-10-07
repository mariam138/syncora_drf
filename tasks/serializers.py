from datetime import datetime
from datetime import timezone as dt_timezone
import pytz
import zoneinfo
from django.utils import timezone
from rest_framework import serializers
from .models import Task


# class ConfigurableModelSerializer(TimezoneMixin, serializers.ModelSerializer):
#     def __init__(self, *args, **kwargs):
#         super(ConfigurableModelSerializer, self).__init__(*args, **kwargs)


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
