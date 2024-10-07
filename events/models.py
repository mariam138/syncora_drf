from django.db import models
from profiles.models import Profile

# Create your models here.

class Event(models.Model):
    """
    Creates an instance of the Event model, which has a many-
    to-one relationship with :model:`profiles.Profile`.
    """
