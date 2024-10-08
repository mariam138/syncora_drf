from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    """Serialises instances of the Note model"""

    owner = serializers.ReadOnlyField(source="owner.user.username")

    class Meta:
        model = Note
        fields = ["id", "owner", "title",
                  "date_created", "date_updated", "content"]
