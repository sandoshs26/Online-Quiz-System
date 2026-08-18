from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import CustomUser

class LoginForm(AuthenticationForm):
    pass 

class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = {
            "username",
            "email",
            "role",
            "phone_number",
            "password1",
            "password2",
        }