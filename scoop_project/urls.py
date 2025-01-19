from django.contrib import admin
from django.urls import path, include

# order of string paths alphabetical, with the empty string path last.
urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path("", include("reviews.urls"), name="reviews-urls"),
]
