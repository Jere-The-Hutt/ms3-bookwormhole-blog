from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Post, Comment, Genre
from .forms import CommentForm


# Create your views here.
class PostList(generic.ListView):
    """
    View to display a paginated list of published blog posts on the homepage.

    - Uses the Post model filtered by status=1 (Published).
    - Orders posts by newest first.
    - Template: reviews/index.html
    """
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "reviews/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display a single published post based on its slug, along with its comments.

    Handles displaying the post and its comments,
    and processing new comment submissions.

    Template: reviews/post_detail.html
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()

    return render(
        request,
        "reviews/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


def comment_edit(request, slug, comment_id):
    """
    View to allow a user to edit their own comment.

    Only the comment's author can make changes. Upon edit,
    the comment is marked as unapproved until re-reviewed.

    Redirects to: post_detail
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!'
                )

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete a comment if the current user is the comment's author.

    Adds a success or error message and redirects to the post's detail page.
    """
    comment = get_object_or_404(Comment, pk=comment_id, post__slug=slug)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def genre_posts(request, slug):
    """
    View to display all posts associated with a specific genre.

    Retrieves posts that match the genre's slug and are published.

    Template: reviews/genre_posts.html
    """
    genre = get_object_or_404(Genre, slug=slug)
    posts = Post.objects.filter(
        genre=genre, status=1).order_by('-created_on')
    return render(
        request, 'reviews/genre_posts.html', {'genre': genre, 'posts': posts})
