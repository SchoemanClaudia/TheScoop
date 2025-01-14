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

    ``reviews``
        An instance of :model:`reviews.ScoopReview`.

    **Template:**

    :template:`reviews/post_detail.html`
    """

    queryset = ScoopReview.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    comments = review.review_location.all().order_by("-created_at")

    return render(
        request,
        "reviews/post_detail.html",
        {
            "review": review,
            "comments": comments,
        },
    )