from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models.newUsers import NewUser
from .models.rutas import Ruta
from .models.reservas import Reserva
from .models.vehiculos import Vehiculo 

admin.site.register(Ruta)
admin.site.register(Reserva)
admin.site.register(Vehiculo)
admin.site.register(NewUser)


