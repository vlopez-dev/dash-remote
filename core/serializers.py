from .models import Equipo,Lectura
from rest_framework import serializers
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('id_equipo','name','direction','state')
        
        
        
class LecturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lectura
        fields = ('id_equipo','fecha_lectura','pro_consum','memory_free')
