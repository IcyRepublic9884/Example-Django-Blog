from django import forms

class CreatePostForm(forms.Form):
    post_title = forms.CharField(label="Title", max_length=80)
    post_content = forms.TextInput()
    post_author = forms.CharField(label="Post As", max_length=100)
