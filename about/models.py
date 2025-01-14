from django.db import models

# Create your models here.

class About(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name