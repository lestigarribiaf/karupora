from django.contrib import admin
from .models import Unidad, Receta, Ingrediente, Insumo, Receta #importamos el modelo
# Register your models here.

admin.site.register(Unidad) # lo registramos
admin.site.register(Ingrediente) 
admin.site.register(Insumo) 
admin.site.register(Receta) 