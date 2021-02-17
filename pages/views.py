from django.shortcuts import render

from .models import Post
from .forms import PostForm, CreatePostForm

def index(request, *args, **kwargs):
    posts = Post.objects.all()
    return render(request, 'pages/index.html', {'title': 'Django-Blog', 'posts': posts})

def about(request, *args, **kwargs):
    # Render the about page
    return render(request, 'pages/about.html', {})

def contact(request, *args, **kwargs):
    # Render the contact pages
    return render(request, 'pages/contact.html', {})

def create_post(request, *args, **kwargs):
    # For the user to make a new post
    # TODO: add the advanced form for this
    # TODO: attach this form to the Django model
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            print("***************************POST VALIDATED AND CREATED")
            print(dir(form))
            return render(request, 'pages/thanks.html', {})
    else:
        form = CreatePostForm()
    return render(request, 'pages/create_post.html', {'form': form})
