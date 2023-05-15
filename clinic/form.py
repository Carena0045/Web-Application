from django.contrib.auth.models import user
from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.emailfield()


class meta:
    model =  user
    fields = ['username','email','password1','password2']

 
