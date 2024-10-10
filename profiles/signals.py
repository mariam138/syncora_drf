# Separate folder for creating signals to keep things modular
# Code for signals to create a Profile instance when a user is created
# Is adapted from: https://dev.to/earthcomfy/django-user-profile-3hik

from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


# User model send signal to Profile model to create
# a profile instance from user instance
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


# Saves the profile instance after creation
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
