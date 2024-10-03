from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    name = serializers.ReadOnlyField(source="user.first_name")
    email = serializers.ReadOnlyField(source="user.email")

    class Meta:
        model = Profile
        fields = ['id', 'username', 'name', 'email', 'created_on', 'updated_on', 'profile_image']
