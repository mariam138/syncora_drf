from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.user.username")
    is_overdue = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = [
            'id',
            'owner',
            'title',
            'due_date',
            'priority',
            'category',
            'description',
            'completed'
        ]