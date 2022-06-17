from django.db.models import fields
from django import forms
from .models import Sysemail,Parameter



class SysemailForm(forms.ModelForm):

    class Meta:
        model=Sysemail
        fields = '__all__'


        # labels = {
        #             'nombre':'Nombre','direccion':'Dirección','telefono':'Teléfono'

        #         }
        
        
        
        
class ParameterForm(forms.ModelForm):
    
    class Meta:
        model=Parameter
        fields = '__all__'