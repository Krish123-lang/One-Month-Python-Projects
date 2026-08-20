from django.shortcuts import render, redirect
from .forms import LoginForm, RegistrationForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
# Create your views here.


def login_user(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('index')
        form = LoginForm()
        return render(request, "users/login_user.html", {'form': form})
    elif request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Hi, {username.title()} ! ")
                return redirect('index')
        messages.error(request, "Invalid username and password")
        return render(request, "users/login_user.html", {'form': form})


def register_user(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request, "users/register_user.html", {'form': form})
    elif request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "You have been registered !")
            login(request, user)
            return redirect('index')
        else:
            return render(request, "users/register_user.html", {'form': form})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully!")
    return redirect('login_user')
