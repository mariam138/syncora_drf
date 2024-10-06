from datetime import datetime
import pytz
from django.utils import timezone
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.user.username")
    is_overdue = serializers.SerializerMethodField()

    def get_is_overdue(self, obj):
        # current_datetime = datetime.datetime.now()
        # current_datetime = current_datetime.astimezone(obj.due_date.tzinfo)

        # utc_duedate = obj.due_date.replace(tzinfo=pytz.utc)

        now = timezone.now()
        # now_1 = now.replace(tzinfo=timezone.utc)
        due_date = obj.due_date
        # due_date = due_date.astimezone(tz=None)
        # now_tz = now.activate()

        print(now)
        # print('utc now', now_1)
        print(due_date)
        # print(current_datetime)

        # if current_datetime > obj.due_date:
        #     obj.is_overdue = True

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