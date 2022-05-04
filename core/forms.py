from django.db.models import fields
from django import forms
from .models import Equipo


class Equipoform(forms.ModelForm):

    class Meta:
        model=Equipo
        fields = '__all__'


        # labels = {
        #             'nombre':'Nombre','direccion':'Dirección','telefono':'Teléfono'

        #         }
