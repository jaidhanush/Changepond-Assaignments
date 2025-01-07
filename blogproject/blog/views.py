from django.shortcuts import render,redirect
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import BloggerForm, PostForm


def create_blogger(request):
    if request.method == 'POST':
        form = BloggerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = BloggerForm()
    return render(request, 'blog/create_blogger.html', {'form': form})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

def homepage(request):
    latest_posts = Post.objects.all().order_by('-date')[:3]
    return render(request, 'blog/homepage.html', {'posts': latest_posts})

def all_blogs(request):
    posts = Post.objects.all()
    return render(request, 'blog/all_blogs.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/blog_detail.html', {'post': post})

