from .models import Equipo
from rest_framework import serializers
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id_equipo','name','direction','pro_consum','memory_free','state')
        
        
        