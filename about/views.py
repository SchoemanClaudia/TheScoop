from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm
# Create your views here.


def meet_us(request):
    """
    Renders the Meet Us page
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.add_message(request, messages.SUCCESS, 
            "Thank you for your message, we will get back to you soon.")

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