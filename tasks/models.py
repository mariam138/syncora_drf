from django.db import models
from profiles.models import Profile

# Create your models here.

PRIORITY_CHOICES = [("L", "Low"), ("M", "Medium"), ("H", "High")]

CATEGORY_CHOICES = [
    ("WORK", "Work"),
    ("PER", "Personal"),
    ("HOME", "Home"),
    ("HEALTH", "Health"),
    ("FIN", "Finance"),
    ("FAM", "Family"),
    ("SOC", "Social"),
    ("EDU", "Learning"),
]


class Task(models.Model):
    """
    Task model with a many-to-one relationship with
    :model:`profiles.Profile`.
    """

    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=255, unique=True)
    due_date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ["due_date"]

    def __str__(self):
        return f"{self.title} | due: {self.due_date}"
