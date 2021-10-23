from django.db.models.base import Model
from rest_framework import serializers
from Transport_apps.models.vehiculos import Vehiculo

class Vehiculo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ('vehiculo_Placa', 'tipo_Vehiculo', 'capacidad_Vehiculo')