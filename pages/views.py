from django.shortcuts import render
from .models import Post

def index(request, *args, **kwargs):
    posts = Post.objects.all()
    return render(request, 'pages/index.html', {'title': 'Random Bullshit', 'posts': posts})

def about(request, *args, **kwargs):
    # Render the about page
    return render(request, 'pages/about.html', {})

def contact(request, *args, **kwargs):
    # Render the contact pages
    return render(request, 'pages/contact.html', {})
