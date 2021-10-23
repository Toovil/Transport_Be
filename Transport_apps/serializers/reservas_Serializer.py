from rest_framework import serializers
from Transport_apps.models.reservas import Reserva

class Reserva_Serializer(serializers.ModelSerializer):
   class Meta:
        model = Reserva
        fields = ['fecha_reserva', 'email']
