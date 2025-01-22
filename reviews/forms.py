from django import forms
from .models import ReviewComment


class CommentForm(forms.ModelForm):
    """
    Submit comment associated with
    :model:`blog.Post` and :model:`auth.User`.
    Data is retrieved from `ReviewComment` model
    then is saved back into `ReviewComment`.
    """
    class Meta:
        model = ReviewComment
        fields = ('comment',)

    # Set the 'comment' field as optional by specifying required=False
    comment = forms.CharField(
        required=True, widget=forms.Textarea(attrs={'rows': 6, 'cols': 40})
        )
