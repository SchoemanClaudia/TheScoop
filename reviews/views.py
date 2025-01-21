from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import ScoopReview, ReviewComment
from .forms import CommentForm


class ReviewList(generic.ListView):
    """
    Display a list of approved :model:`reviews.ScoopReview`.

    **Context**
    ``reviews``
        A list of :model:`reviews.ScoopReview` 
        objects with status=1.

    **Template:**
    :template:`reviews/index.html`
    """
    queryset = ScoopReview.objects.filter(status=1)
    template_name = "reviews/index.html"
    paginate_by = 3


def post_detail(request, slug):
    """
    Display an individual :model:`reviews.ScoopReview`.

    **Context**
    ``reviews``
        An instance of :model:`reviews.ScoopReview` 
        retrieved by slug.
    ``comments``
        A list of :model:`reviews.ReviewComment` 
        associated with the review.
    ``comment_count``
        The count of approved comments for the review.
    ``comment_form``
        An instance of :model:`reviews.CommentForm` 
        for submitting new comments.

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
            # If form is valid, save the comment
            comment = comment_form.save(commit=False)
            comment.critic = request.user
            comment.review = review
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment is submitted & awaiting approval.'
            )
            # Redirect after submit success, clear form to avoid resubmit
            return HttpResponseRedirect(reverse('review_detail', args=[slug]))
    else:
        # Populate new empty form (for GET request)
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


def comment_edit(request, slug, comment_id):
    """
    Edit an existing :model:`reviews.ReviewComment`.

    **Context**
    ``review``
        The :model:`reviews.ScoopReview` 
        associated with the comment.
    ``comment``
        The :model:`reviews.ReviewComment` 
        being edited.
    ``comment_form``
        An instance of :model:`reviews.CommentForm` 
        for editing the comment.

    **Template:**
    :template:`reviews/post_detail.html`
    """
    # Fetch the review and comment
    review = get_object_or_404(ScoopReview, slug=slug)
    comment = get_object_or_404(ReviewComment, pk=comment_id)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.critic == request.user:
            # Save updated comment, still needs admin review
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.accept = False
            comment.save()
            messages.success(request, 'Comment Updated!')
            return HttpResponseRedirect(reverse('review_detail', args=[slug]))
        else:
            messages.error(request, 'Error updating comment!')
    else:
        # Populate form with existing comment data (for GET request)
        comment_form = CommentForm(instance=comment)

    return render(
        request,
        # Render new post_detail.html template
        "reviews/post_detail.html",
        {
            "review": review,
            "comment_form": comment_form,
            "comment_editing": True,
            "comment": comment
        }
    )


def comment_delete(request, slug, comment_id):
    """
    Delete a :model:`reviews.ReviewComment`.

    **Context**
    ``review``
        The :model:`reviews.ScoopReview` 
        associated with the comment.
    ``comment``
        The :model:`reviews.ReviewComment` 
        being deleted.

    **Template:**
    :template:`reviews/post_detail.html`
    """
    queryset = ScoopReview.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(ReviewComment, pk=comment_id)

    if comment.critic == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))
