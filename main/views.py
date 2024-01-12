from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.models import User



def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username        = request.POST['username']
        password        = request.POST['password']
        passwordCheck   = request.POST['passwordCheck']

        if password == passwordCheck:
            # Verifica si el usuario ya existe
            if not User.objects.filter(username=username).exists():
                # Crea un nuevo usuario
                user = User.objects.create_user(
                    username=username, password=password
                    )
                login(request, user)
                return redirect('home')  # Redirige a la página de inicio
            else:
                # El usuario ya existe, manejarlo según sea necesario
                messages.success(request, 'The user exist')
                return render(request, 'registration/register.html')
        else:
            messages.success(request, 'The password not is')
            return render(request, 'registration/register.html')
    else:
        return render(request, 'registration/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        
        else:
            try:
                user = User.objects.get(username=username)
                messages.success(request, 'The password is incorrect')
            except User.DoesNotExist:
                messages.success(request, 'User doesnt exist')
            return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')

def user_logout(request):
    logout(request)
    return redirect('home')