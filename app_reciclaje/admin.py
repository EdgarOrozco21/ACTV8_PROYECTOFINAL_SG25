from django.contrib import admin
from .models import CentroAcopio, Donante, EmpleadoReciclaje, MaterialReciclable, RecepcionMaterial

admin.site.register(CentroAcopio)
admin.site.register(Donante)
admin.site.register(EmpleadoReciclaje)
admin.site.register(MaterialReciclable)
admin.site.register(RecepcionMaterial)
