from core.models import Configuration
from rest_framework import serializers
class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ('id_config','email','passemail','recivedemail','contentemail')
        
        
        