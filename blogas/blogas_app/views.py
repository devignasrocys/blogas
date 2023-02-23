from django.shortcuts import render,get_object_or_404
from django.views import generic
from . import models

# Create your views here.
def index(request):
    posts = models.Post.objects.all()
    return render(request, 'blog/index.html', {
        "all_posts": posts,
    }
    )


class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = "blog/post.html"

