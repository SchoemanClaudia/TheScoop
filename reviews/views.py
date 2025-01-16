from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
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
    total_upvotes = sum(comment.upvotes for comment in comments)
    total_downvotes = sum(comment.downvotes for comment in comments)

    if request.method == "POST":
        print("Received a POST request")
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.critic = request.user
            comment.review = review
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment is submitted & awaiting approval'
    )

    comment_form = CommentForm(data=request.POST)
    print("About to render template")
    

    return render(
        request,
        "reviews/post_detail.html",
        {
            "review": review,
            "comments": comments,
            "comment_count": comment_count,
            "total_upvotes": total_upvotes,
            "total_downvotes": total_downvotes,
            "comment_form": comment_form,
        },
    )
    

def comment_edit(request, slug, comment_id):
    """
    view to edit comments
     """
    if request.method == "POST":

        queryset = ScoopReview.objects.filter(status=1)
        review = get_object_or_404(ScoopReview, slug=slug)
        comment = get_object_or_404(ReviewComment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.critic == request.user:
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.accept = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 
                'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                'Error updating comment!')

    return HttpResponseRedirect(reverse('review_detail', args=[slug]))