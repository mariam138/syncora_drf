from rest_framework import serializers
from .models import Event


class EventSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.user.username")
    """
    Display human readable label for category choices. This is used for the
    front end display. Code adapted from
    https://github.com/encode/django-rest-framework/issues/1755#issuecomment-945167944
    and the comment below it.
    """
    category_display = serializers.CharField(source="get_category_display", read_only=True)
    date = serializers.DateField(format="%Y-%m-%d")

    # Ensure event name is capitalised
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['name'] = rep["name"].capitalize()
        return rep

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
            "category_display",
            "location",
            "notes",
        ]
