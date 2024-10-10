from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.user.username")

    class Meta:
        model = Event
        fields = [
            "id",
            "owner",
            "name",
            "date",
            "start_time",
            "end_time",
            "category",
            "location",
            "notes"
        ]
