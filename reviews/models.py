from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class ScoopReview(models.Model):
    heading = models.CharField(max_length=200, unique=True)
    blurb = models.SlugField(max_length=200, unique=True)
    review = models.TextField()
    rating = models.IntegerField()
    critic = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_posts")
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)