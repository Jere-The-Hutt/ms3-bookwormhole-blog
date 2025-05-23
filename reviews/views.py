from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post


# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "reviews/index.html"
    paginate_by = 6


def post_detail(request, slug):
    """
    Display a single published post based on its slug.

    Template: reviews/post_detail.html
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    return render(
        request,
        "reviews/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
        }
    )
