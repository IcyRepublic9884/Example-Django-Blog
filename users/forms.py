from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=80, widget=forms.TextInput(attrs={'class': 'form-control '}))
    password = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control '}))
