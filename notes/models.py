from django.db import models
from profiles.models import Profile

# Create your models here.


class Note(models.Model):
    """
    Allows user to create an instance of a note in relation to
    :model:`profiles.Profile`. The title is optional to allow
    user to focus solely on the content if they need to make a
    quick note.
    """

    owner = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=250, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        """ Orders notes showing the most recently updated at the top """
        ordering = ["-date_updated"]

    def __str__(self):
        """ Will show title if available and a preview of the content """
        return f"{self.title} | {self.content[:25]}..."
