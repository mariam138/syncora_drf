from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    """
    Serialises the data from :model:`profiles.Profile` into JSON format.
    username, name and email are custom read only fields with the source
    stemming from the fields in the User model.
    """
    username = serializers.ReadOnlyField(source="user.username")
    name = serializers.ReadOnlyField(source="user.first_name")
    email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Profile
        fields = ['id', 'username', 'name', 'email', 'created_on', 'updated_on', 'profile_image']
