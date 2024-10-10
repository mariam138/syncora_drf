from django.db import models
from location_field.models.plain import PlainLocationField
from profiles.models import Profile

# Create your models here.

CATEGORY_CHOICES = [
    ("WORK", "Work"),
    ("SOC", "Social"),
    ("FAM", "Family"),
    ("APP", "Appointment"),
    ("EDU", "Education"),
    ("TRAVEL", "Travel"),
]


class Event(models.Model):
    """
    Creates an instance of the Event model, which has a many-
    to-one relationship with :model:`profiles.Profile`.
    """

    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="events")
    name = models.CharField(max_length=250, unique=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES)
    location = PlainLocationField(based_fields=["city"], zoom=7)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.name} | {self.date}"
