from django.shortcuts import render
from .models import About
from .forms import CollaborateForm
# Create your views here.


def meet_us(request):
    """
    Renders the Meet Us page
    """
    about = About.objects.all().order_by('-updated_at').first()
    collaborate_form = CollaborateForm()

    return render(
        request,
        "about/meet_us.html",
        {
            "about": about,
            "collaborate_form": collaborate_form,
        },
    )