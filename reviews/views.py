from django.shortcuts import render
from django.views import generic
from .models import ScoopReview

# Create your views here.
class ReviewList(generic.ListView):
    queryset = ScoopReview.objects.filter(status=1)
    template_name = "reviews/index.html"
    paginate_by = 3
