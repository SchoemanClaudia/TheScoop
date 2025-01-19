from . import views
from django.urls import path

urlpatterns = [
    path('', views.meet_us, name='about'),
]
