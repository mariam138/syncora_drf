from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="profile.user.username")

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