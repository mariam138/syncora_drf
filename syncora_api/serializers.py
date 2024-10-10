from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer


class CustomRegisterSerializer(RegisterSerializer):
    """
    Overrides the basic dj-rest-auth registration by adding a first_name
    field to the registration form. This makes it mandatory when signing up,
    making it easier to be made a part of the profile instance for use
    in the front-end. Code adapted from:
    https://stackoverflow.com/questions/62291394/django-rest-auth-dj-rest-auth-custom-user-registration
    """

    first_name = serializers.CharField()

    def save(self, request):
        user = super().save(request)
        user.first_name = self.validated_data.get("first_name")
        user.save()
        return user
