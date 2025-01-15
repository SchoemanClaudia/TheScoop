from .models import ReviewComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = ReviewComment
        fields = ('comment',)