from .models import Sysemail
from rest_framework import serializers
class SysemailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sysemail
        fields = ('id_config','email','passemail','recivedemail','contentemail')
        
        
        