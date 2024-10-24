from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.registration.views import RegisterView


class CustomRegisterSerializer(RegisterSerializer):
    """
    Overrides the basic dj-rest-auth registration by adding a first_name
    field to the registration form. This makes it mandatory when signing up,
    making it easier to be made a part of the profile instance for use
    in the front-end. Code adapted from:
    https://stackoverflow.com/questions/36910373/django-rest-auth-allauth-registration-with-email-first-and-last-name-and-witho
    """

    first_name = serializers.CharField(required=True)

    def get_cleaned_data(self):
        cleaned_data = super().get_cleaned_data()  # Get the cleaned data from the parent class
        cleaned_data['first_name'] = self.validated_data.get('first_name')
        return cleaned_data

    def custom_signup(self, request, user):
        user.first_name = self.validated_data.get('first_name', '')
        user.save(update_fields=['first_name',])


class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer