from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serialises the data from :model:`profiles.Profile` into JSON format.
    username, name and email are custom read only fields with the source
    stemming from the fields in the User model. List view has read-only
    access as this view is being used for testing purposes only while
    building the API.
    """

    username = serializers.ReadOnlyField(source="user.username")
    name = serializers.ReadOnlyField(source="user.first_name")
    email = serializers.ReadOnlyField(source="user.email")
    is_owner = serializers.SerializerMethodField()
    notes_count = serializers.ReadOnlyField()
    tasks_count = serializers.ReadOnlyField()
    events_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        # Checks to see if the currently logged in user
        # is the owner of the object
        # Can be useful later on in the front-end for certain UI aspects
        # Code adapted from Code Institute's 'Authentication,
        # authorization and serializer
        # method fields' video in the Django REST framework module
        request = self.context["request"]
        return request.user == obj.user

    # def validate_profile_image(self, value):
    #     """Custom validator for uploading a profile picture, ensuring it is
    #     less than 2MB in size. Code adopted from Code Institute's Django REST
    #     Framework module when creating the post serialiser."""
    #     if value.size > 1024 * 1024 * 2:
    #         raise serializers.ValidationError(
    #             "Image cannot be larger than 2MB."
    #             "Please choose a smaller image."
            # )

    class Meta:
        model = Profile
        fields = [
            "id",
            "username",
            "name",
            "email",
            "created_on",
            "updated_on",
            "profile_image",
            "is_owner",
            "events_count",
            "tasks_count",
            "notes_count",
        ]
