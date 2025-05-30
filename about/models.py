from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class About(models.Model):
    """
    Represents the 'About' section of the website, including a title,
    profile image, and descriptive body content.
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    body = models.TextField()

    def __str__(self):
        return self.title
