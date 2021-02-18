from django import forms
from .models import Post

class CreatePostForm(forms.Form):
    post_title = forms.CharField(label="Title", max_length=80)
    post_content = forms.CharField(widget=forms.Textarea)
    post_author = forms.CharField(label="Post As", max_length=100)

    def __str__(self):
        return self.post_title

# Trying Something new here
class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control '}))
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control '}))
    author = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control '}))
    class Meta:
        model = Post
        fields = ['author', 'title', 'content']
