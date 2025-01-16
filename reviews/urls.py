from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('review/<slug:slug>/', views.post_detail, name='review_detail'),
]