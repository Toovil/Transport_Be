from rest_framework import serializers
from Transport_apps.models.reservas import Reserva

class Reserva_Serializer(serializers.ModelSerializer):
   class Meta:
        model = Reserva
        fields = ['fecha_reserva', 'email']

        def to_representation(self, obj):
            reserva = Reserva.objects.get(id=obj.email)
            return {
               'fecha_reserva' : Reserva.fecha_reserva,
               'email' : Reserva.email
            }
