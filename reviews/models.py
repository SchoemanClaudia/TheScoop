from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from cloudinary.models import CloudinaryField


# Choices are a sequence of 2-tuples
STATUS = ((0, "Draft"), (1, "Published"))


class ScoopReview(models.Model):
    """
    Stores review of a location, including rating,
    review text, and image, related to :model:`auth.User`.
    Data retrieved from critic review of a location
    and includes an optional map URL.
    """
    location = models.CharField(max_length=200, unique=True)
    blurb = models.CharField(max_length=100, blank=True)
    slug = models.SlugField(max_length=100, unique=True)
    featured_image = CloudinaryField('image', default='placeholder')
    directions = models.URLField(
        max_length=2000, blank=True, unique=True, null=True,
        help_text="Map URL goes here"
        )
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

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.location} | rated {self.rating} by {self.critic}"


class ReviewComment(models.Model):
    """
    Stores comment on a specific review, related to
    :model:`blog.ScoopReview` and :model:`auth.User`.
    Data retrieved from critic comment on a location
    review and includes a flag to be reviewed and accepeted.
    """
    review = models.ForeignKey(
        ScoopReview, on_delete=models.CASCADE, related_name="review_location")
    critic = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    accept = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Comment {self.comment} by {self.critic}"
