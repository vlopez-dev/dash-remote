from django.db.models import fields
from django import forms
from .models import Sysemail



class SysemailForm(forms.ModelForm):

    class Meta:
        model=Sysemail
        fields = '__all__'


        # labels = {
        #             'nombre':'Nombre','direccion':'Dirección','telefono':'Teléfono'

        #         }