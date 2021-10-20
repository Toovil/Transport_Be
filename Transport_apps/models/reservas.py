from django.db import models
from Transport_apps.models.newUsers import NewUser
from django.db.models.deletion import CASCADE


class Reserva(models.Model):
    reserva_id = models.AutoField(primary_key=True)
    fecha_reserva = models.DateTimeField()
    email = models.ForeignKey(NewUser, on_delete=models.CASCADE)