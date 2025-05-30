from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for submitting a comment on a blog post.
    Only includes the comment body field.
    """
    class Meta:
        model = Comment
        fields = ('body',)
