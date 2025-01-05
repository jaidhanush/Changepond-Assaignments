from django.shortcuts import render
from .models import Post
from django.shortcuts import get_object_or_404

def homepage(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/homepage.html', {'posts': latest_posts})

def all_blogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/all_blogs.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})
