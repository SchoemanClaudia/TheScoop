from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About, CollaborateRequest


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface for :model:`app.About`, 
    Stores information about the user biography. 
    Data for 'bio' is edited using the Summernote widget.
    """
    summernote_fields = ('bio',)

# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    Admin interface for :model:`app.CollaborateRequest`, 
    Stores collaboration requests from users.
    Related to :model:`auth.User` and :model:`app.Post` .
    """
    list_display = ('message', 'read',)
