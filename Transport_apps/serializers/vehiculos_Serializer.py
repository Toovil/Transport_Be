from django.db.models.base import Model
from rest_framework import serializers
from Transport_apps.models.vehiculos import Vehiculo

class Vehiculo_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ('vehiculo_Placa', 'tipo_Vehiculo', 'capacidad_Vehiculo')

        def to_representation(self, obj):
            vehiculo = Vehiculo.objects.get(id=obj.vehiculo_Placa)
            return {
                'vehiculo_Placa' : Vehiculo.vehiculo_Placa,
                'tipo_Vehiculo' : Vehiculo.tipo_Vehiculo,
                'capacidad_Vehiculo' : Vehiculo.capacidad_Vehiculo
            }