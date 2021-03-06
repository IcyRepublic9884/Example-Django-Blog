from django import forms
from .models import Post

# Trying Something new here
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control '}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control '}))
    author = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control '}))
    class Meta:
        model = Post
        fields = ['author', 'title', 'content']
