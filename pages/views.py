from django.shortcuts import render
from django.template import loader
from django.http import Http404

def index(request, *args, **kwargs):
    return render(request, 'pages/index.html', {'title': 'Random Bullshit'})
