from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm

def register(request, *args, **kwargs):
    """Register the user"""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account Created For '{username}' You can now login")
            return redirect('users-login-page')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request, *args, **kwargs):
    return render(request, 'users/profile.html', {})
