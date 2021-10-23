from rest_framework import serializers
from Transport_apps.models.rutas import Ruta

class Ruta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = ['origen', 'destino', 'vehiculo_placa', 'reserva_id']

