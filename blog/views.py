from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

# Create your views here.

class PostList(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.order_by('-created')

# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts': posts})


