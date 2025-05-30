from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for users to submit book review suggestions or contact messages.

    Uses the Contact model to collect:
    - name
    - email
    - book title and author
    - message content
    """
    class Meta:
        model = Contact
        fields = ['name', 'email', 'book_title', 'book_author', 'message']
