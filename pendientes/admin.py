from django.contrib import admin
from .models import Tarea, Receta #importamos el modelo

# Register your models here.

admin.site.register(Tarea) # lo registramos
admin.site.register(Receta) 