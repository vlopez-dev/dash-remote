from django.db.models import fields
from django import forms
from .models import Equipo


class Equipoform(forms.ModelForm):
    passwordadmin = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model=Equipo
        fields = ['name', 'direction','user_admin','passwordadmin']

  
        labels = {
            'name':'Nombre','direction':'Direccion Ip','user_admin':'Administrador','passwordadmin':'Password'
        }


class Mensajeform(forms.Form):
    mensaje= forms.CharField(max_length=500,widget=forms.Textarea(attrs={'name':'body', 'rows':10, 'cols':50}))