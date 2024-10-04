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

    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            "username": self.validated_data.get("username", ""),
            "first_name": self.validated_data.get("first_name", ""),
            "email": self.validated_data.get("email", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
        }
