from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [ 'first_name', 'username', 'email', 'password1', 'password2']



from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # Puedes personalizar el formulario según tus necesidades
    pass
