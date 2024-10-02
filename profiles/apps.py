from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'

    # This overrides the ready() method for the app config by registering
    # the signals created
    # Code adapted from: https://dev.to/earthcomfy/django-user-profile-3hik
    def ready(self):
        import profiles.signals
