from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """
    Profile model with a one to one relationship with :model:`auth.User`
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    profile_image = models.ImageField(
        upload_to='images/syncora-profile-images/', default='../avatar-default_lxccrh'
    )

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f"{self.user}'s profile"