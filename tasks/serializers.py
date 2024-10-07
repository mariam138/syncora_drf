from datetime import datetime
import pytz
import zoneinfo
from django.utils import timezone
from rest_framework import serializers
from .models import Task


class TimezoneMixin:
    def initial(self, request, *args, **kwargs):
        super().initial(request, *args, **kwargs)

        tzname = request.user.time_zone if request.user.is_authenticated else None
        # if request.user.is_authenticated:
        #     tzname = request.user.timezone
        #     # print('Mixin', tzname)
        if tzname:
            timezone.activate(zoneinfo.ZoneInfo(tzname))
        else:
            timezone.deactivate()


class ConfigurableModelSerializer(TimezoneMixin, serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super(ConfigurableModelSerializer, self).__init__(*args, **kwargs)


class TaskSerializer(ConfigurableModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.user.username")
    is_overdue = serializers.SerializerMethodField()

    def get_is_overdue(self, obj):
        # current_datetime = datetime.datetime.now()
        # current_datetime = current_datetime.astimezone(obj.due_date.tzinfo)

        # utc_duedate = obj.due_date.replace(tzinfo=pytz.utc)

        now = timezone.now()
        # is_now_aware = now.timezone.is_aware
        # now_1 = now.replace(tzinfo=timezone.utc)
        due_date = obj.due_date
        # due_date = due_date.astimezone(tz=None)
        # now_tz = now.activate()

        # request = self.context["request"]
        # tz = request.user.time_zone

        print("Current time:", now)
        # print(is_now_aware)
        # print('utc now', now_1)
        print("Due date:", due_date)
        # print(tz)
        # print(current_datetime)

        # if current_datetime > obj.due_date:
        #     obj.is_overdue = True

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
            "is_overdue",
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