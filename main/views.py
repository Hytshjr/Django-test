
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages


def user_not_authenticated(user):
    return not user.is_authenticated


def index(request):
    return render(request, 'home.html')


@user_passes_test(user_not_authenticated, login_url='home')
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['passwordCheck']

        if not username:
            messages.error(request, 'Username cannot be empty')
        elif not password:
            messages.error(request, 'Password cannot be empty')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif password != password_check:
            messages.error(request, 'Passwords do not match')
        else:
            # Crear un nuevo usuario
            user = User.objects.create_user(
                username=username, password=password
                )
            login(request, user)
            return redirect('home') # Redirige a la página de inicio

    return render(request, 'registration/register.html')


@user_passes_test(user_not_authenticated, login_url='home')
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')
        elif not username:
            messages.error(request, 'Username cannot be empty')
        elif not password:
            messages.error(request, 'Password cannot be empty')
        elif not User.objects.filter(username=username).exists():
            messages.error(request, 'Username not exists')
        else:
            messages.error(request, 'Password is incorrect')

    return render(request, 'registration/login.html')


def user_logout(request):
    logout(request)
    return redirect('home')