from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Choices are a sequence of 2-tuples
STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class ScoopReview(models.Model):
    location = models.CharField(max_length=200, unique=True)
    blurb = models.SlugField(max_length=200, unique=True)
    review = models.TextField()
    # Rating out of 5
    rating = models.DecimalField(
        # Up to 2 digits with 1 decimal place (eg. 3.5)
        max_digits=3,
        decimal_places=1,
        validators=[
            MinValueValidator(1.0),
            MaxValueValidator(5.0),
        ],
        # Set default rating
        default=5.0,
    )
    critic = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="review_posts")
    created_at = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)