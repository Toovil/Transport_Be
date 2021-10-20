from django.db import models

class Vehiculo(models.Model):
    vehiculo_Placa = models.CharField(max_length=200, primary_key=True)
    tipo_Vehiculo = models.CharField(max_length=200)
    capacidad_Vehiculo = models.IntegerField()