from django.db.models import fields
from django import forms
from .models import Sysemail,Parameter



class SysemailForm(forms.ModelForm):
    contentemail= forms.CharField(max_length=500,widget=forms.Textarea(attrs={'name':'body', 'rows':10, 'cols':50}))
    class Meta:
        model=Sysemail
        fields = '__all__'

        
        
        labels = {
                    'email':'E-mail','passemail':'Password','recivedemail':'Email Receptor','subject':'Asunto','contentemail':'Contenido','time_mail':'Tiempo de envio'

                }
        
        
        
class ParameterForm(forms.ModelForm):
    
    class Meta:
        model=Parameter
        fields = '__all__'
        
        
        

        labels = {
                    'time_check':'Tiempo'

                }
        