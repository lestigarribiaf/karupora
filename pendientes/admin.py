from django.contrib import admin
from .models import Tarea, Recetas #importamos el modelo

# Register your models here.

admin.site.register(Tarea) # lo registramos
admin.site.register(Recetas) 