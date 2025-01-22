from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm


def meet_us(request):
    """
    Renders the Meet Us page.

    **Context**
    ``about``
        Displays an individual instance of :model:`about.About`
        containing the most recent 'About' information,
        ordered by `updated_at` in descending order.
    ``collaborate_form``
        An instance of :forms:`about.CollaborateForm`,
        used for submitting collaboration inquiries.

    **Template:**
    :template:`about/meet_us.html`
    """
    if request.method == "POST":
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(request, "Your message was sent successfully.")

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
