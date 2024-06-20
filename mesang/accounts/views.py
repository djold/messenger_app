import profile
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from subscribers.models import SubscribeModel
from .forms import RegisterForm, LoginForm
from .models import UserProfile


# Create your views here.

def register_view(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')
        email = form.cleaned_data.get('email')
        user = User.objects.create_user(user_name, email, password)
        user.save()
        profile = UserProfile(profile=user)
        profile.save()
        login(request, user)
        return redirect("/")
    return render(request, 'accounts/registration.html', {'form': form})

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user_name = form.cleaned_data.get('user_name')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=user_name, password=password)
        if user:
            login(request, user)
            return redirect("/")
    return render(request, 'accounts/login_form.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect("/")

def profile_view(request):
    friends_list = SubscribeModel.objects.filter(self_user=request.user)
    return render(request, 'accounts/profile.html', {'friends_list': friends_list})




