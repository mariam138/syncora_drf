from django.db import models
from location_field.models.plain import PlainLocationField
from profiles.models import Profile

# Create your models here.

class Event(models.Model):
    """
    Creates an instance of the Event model, which has a many-
    to-one relationship with :model:`profiles.Profile`.
    """
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    date = models.DateField(widget=DateInput)
    start_time = models.DurationField(widget=TimeInput)
    end_time = models.DurationField(widget=TimeInput)
    category = models.CharField(max_length=30, CHOICES)
    location = PlainLocationField(based_fields=['city'], zoom=7)
    notes = models.TextField(blank=True)
