from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="user.username")
    profile_id = serializers.ReadOnlyField(source="user.profile.id")

    class Meta:
        model = Task
        fields = [
            'id',
            'owner',
            'profile_id',
            'title',
            'due_date',
            'priority',
            'category',
            'description',
            'completed'
        ]