from django.db.models import fields
from django import forms
from .models import Equipo


class Equipoform(forms.ModelForm):
    passwordadmin = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Equipo
        fields = ['name', 'direction','user_admin','passwordadmin']

