from django.shortcuts import render

from .models import Post
from .forms import PostForm

def index(request, *args, **kwargs):
    # posts = Post.objects.all()
    return render(request, 'pages/index.html', {'title': 'Django-Blog', 'posts': None})

def about(request, *args, **kwargs):
    # Render the about page
    return render(request, 'pages/about.html', {})

def contact(request, *args, **kwargs):
    # Render the contact pages
    return render(request, 'pages/contact.html', {})

def create_post(request, *args, **kwargs):
    # For the user to make a new post
    # TODO: Use django-crispy-forms
    if request.method == 'POST':
        # If the User has filled the form, and clicked submit
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'pages/thanks.html', {})
    else:
        form = PostForm()
    return render(request, 'pages/create_post.html', {'form': form})
