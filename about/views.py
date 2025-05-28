from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from contact.forms import ContactForm


def about_me(request):
    """
    Renders the About page and processes Contact form submissions
    """
    about = About.objects.all().order_by('-updated_on').first()
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks! Your suggestion has been submitted.")
            return redirect("about")

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "form": form,
        },
    )
