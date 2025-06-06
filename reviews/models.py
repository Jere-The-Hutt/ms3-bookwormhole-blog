from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Genre(models.Model):
    """
    Represents a book genre category.
    Used to classify blog posts.
    """
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Represents a blog post (book review), including title, content, genre,
    author, image, excerpt, status, and timestamps.
    """
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(
        Genre, on_delete=models.SET_NULL, null=True, related_name='posts'
        )
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reviews_posts"
        )
    featured_image = CloudinaryField('image', default='placeholder')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Returns the post title along with the author's name.
        """
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Represents a user comment on a blog post. Includes author, body, timestamp,
    and approval status.
    """
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
        )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        """
        Returns a string representation of the comment and its author.
        """
        return f"Comment {self.body} by {self.author}"
