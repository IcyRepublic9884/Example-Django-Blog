from django import forms
from .models import Post

class CreatePostForm(forms.Form):
    post_title = forms.CharField(label="Title", max_length=80)
    post_content = forms.CharField(widget=forms.Textarea)
    post_author = forms.CharField(label="Post As", max_length=100)

# Trying Something new here
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'title', 'content']
