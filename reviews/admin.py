from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ScoopReview, ReviewComment


@admin.register(ScoopReview)
class ReviewsAdmin(SummernoteModelAdmin):
    """
    Review entry related to:
      - :model:`auth.User`, user who created review
      - :model:`location.Location`, location of review
    Data fetched from ScoopReview model and displayed
    within admin interface
    """
    list_display = ('location', 'status', 'critic', 'created_at')
    search_fields = ['location', 'review']
    list_filter = ('critic', 'status', 'created_at')
    prepopulated_fields = {'slug': ('location',)}
    summernote_fields = ('review',)


admin.site.register(ReviewComment)
"""
Stores a comment entry related to
:model:`auth.User` and :model:`blog.Post`.
Data is fetched from the ReviewComment model
and displayed in the admin interface.
"""
