from .models import ReviewComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = ReviewComment
        fields = ('comment',)

    # Set the 'comment' field as optional by specifying required=False
    comment = forms.CharField(required=True, widget=forms.Textarea(attrs={'rows': 6, 'cols': 40}))