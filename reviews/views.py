from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import ScoopReview

# Create your views here.
class ReviewList(generic.ListView):
    queryset = ScoopReview.objects.filter(status=1)
    template_name = "reviews/index.html"
    paginate_by = 3


def post_detail(request, slug):
    """
    Display an individual :model:`reviews.ScoopReview`.

    **Context**

    ``post``
        An instance of :model:`reviews.ScoopReview`.

    **Template:**

    :template:`reviews/post_detail.html`
    """

    queryset = ScoopReview.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "reviews/post_detail.html",
        {"post": post},
    )