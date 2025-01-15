from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import ScoopReview, ReviewComment
from .forms import CommentForm

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
    comment_count = review.review_location.filter(accept=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.critic = request.user
            comment.review = review
            comment.save()

    comment_form = CommentForm()
    

    return render(
        request,
        "reviews/post_detail.html",
        {
            "review": review,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )