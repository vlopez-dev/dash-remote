from .models import Equipo
from rest_framework import serializers
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = ('name','direction','state','memory_free', 'pro_consum')