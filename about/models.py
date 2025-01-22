from django.db import models
from cloudinary.models import CloudinaryField


class About(models.Model):
    """
    Stores information about an individual,
    including user name, bio and avatar image.
    """
    name = models.CharField(max_length=200)
    bio = models.TextField()
    avatar_image = CloudinaryField('image', default='placeholder')
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class CollaborateRequest(models.Model):
    """
    Stores a collaboration request with a
    name, email, message, and a flag indicating
    whether the request has been read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"
