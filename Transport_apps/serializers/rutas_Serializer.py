from rest_framework import serializers
from Transport_apps.models.rutas import Ruta

class Ruta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Ruta
        fields = ['origen', 'destino', 'vehiculo_placa', 'reserva_id']

        def to_representation(self, obj):
            ruta = Ruta.objects.get(id=obj.email)
            return {
                'origen' : Ruta.origen,
                'destino' : Ruta.destino,
                'vehiculo_placa' : Ruta.vehiculo_placa,
                'reserva_id': Ruta.reserva_id
            }
