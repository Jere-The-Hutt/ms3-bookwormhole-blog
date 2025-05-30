from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from contact.forms import ContactForm


def about_me(request):
    """
    Display the About page and handle contact form submissions.

    - Retrieves the latest About content to display.
    - Initializes and processes the ContactForm.
    - If the form is submitted and valid,
      saves it and displays a success message.
    - Redirects to the About page on successful submission.

    Template: about/about.html
    Context:
        - 'about': latest About instance
        - 'form': ContactForm instance
    """
    about = About.objects.all().order_by('-updated_on').first()
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Thanks! Your suggestion has been submitted."
                )
            return redirect("about")

    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "form": form,
        },
    )
