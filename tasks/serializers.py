import datetime
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.user.username")
    is_overdue = serializers.SerializerMethodField()

    def get_is_overdue(self, obj):
        current_datetime = datetime.datetime.now()

        if current_datetime > obj.due_date:
            obj.is_overdue = True

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
            'is_overdue',
            'completed'
        ]