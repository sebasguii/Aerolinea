from django import forms
from .models import Avion
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AvionCreationForm
from django.contrib.auth.models import User
# from django.contrib.auth.models import Avion

#formulario para productos

class AvionForm(forms.ModelForm):
    class Meta:
        model = Avion
        fields= '__all__'

#Formulario para registro de usuarios

class RegistroUsuariosForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']