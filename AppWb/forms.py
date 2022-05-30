from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from AppWb.models import Avatar
class EquiposFormularios(forms.Form):
    nombre=forms.CharField(max_length=30)

    seguidores=forms.IntegerField()
class AsociadosFormularios(forms.Form):
    nombre=forms.CharField(max_length=30)
    redes_sociales=forms.CharField(max_length=30)
class CursosFormularios(forms.Form):
        nombre=forms.CharField(max_length=50)
        jugadorpro=forms.CharField(max_length=40)
        duracion=forms.CharField(max_length=40)
class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita la contraseña', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields= ['username','email','password1','password2']

    