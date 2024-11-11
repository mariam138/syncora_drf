from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serialises instances of the Note model"""

    owner = serializers.ReadOnlyField(source="owner.user.username")
    date_created = serializers.DateTimeField(format="%d %b %Y, %H:%M")
    date_updated = serializers.DateTimeField(format="%d %b %Y, %H:%M")

    class Meta:
        model = Note
        fields = ["id", "owner", "title",
                  "date_created", "date_updated", "content"]
