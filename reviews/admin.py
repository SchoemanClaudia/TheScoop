from django.contrib import admin
from .models import ScoopReview, ReviewComment

# Register your models here.
admin.site.register(ScoopReview)
admin.site.register(ReviewComment)