from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    A form to handle collaboration requests.
    Collects data from the user including
    name, email, and message, which are stored
    in the `CollaborateRequest` model.
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
