from django.db import models


# Create your models here.
class Contact(models.Model):
    """
    Stores contact form submissions from users, including their name,
    email, a recommended book title and author,
    a message, and the submission timestamp.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    book_title = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.book_title}"
