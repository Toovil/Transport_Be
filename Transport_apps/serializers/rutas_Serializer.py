from rest_framework import serializers
from Transport_apps.models.rutas import Ruta

class Ruta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = ['origen', 'destino', 'vehiculo_placa', 'reserva_id']

        def to_representation(self, obj):
            ruta = Ruta.objects.get(id=obj.email)
            return {
                'origen' : ruta.origen,
                'destino' : ruta.destino,
                'vehiculo_placa' : ruta.vehiculo_placa,
                'reserva_id': ruta.reserva_id
            }
