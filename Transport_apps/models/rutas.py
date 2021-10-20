from django.db import models
from django.db.models.deletion import CASCADE
from .vehiculos import Vehiculo
from .reservas import Reserva

class Ruta(models.Model):
    id = models.AutoField(primary_key=True)
    origen = models.CharField(max_length=200)
    destino = models.CharField(max_length=200)
    vehiculo_placa = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    reserva_id = models.ForeignKey(Reserva, on_delete=models.CASCADE)