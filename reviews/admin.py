from django.contrib import admin
from .models import ScoopReview, ReviewComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(ScoopReview)
class ReviewsAdmin(SummernoteModelAdmin):
    
    list_display = ('location', 'directions', 'status', 'created_at')
    search_fields = ['location', 'review']
    list_filter = ('status', 'created_at')
    prepopulated_fields = {'slug': ('location',)}
    summernote_fields = ('review',)


# Register your models here.
admin.site.register(ReviewComment)