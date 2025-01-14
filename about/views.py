from django.shortcuts import render
from .models import About
# Create your views here.


def meet_us(request):
    """
    Renders the Meet Us page
    """
    about = About.objects.all().order_by('-updated_at').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )