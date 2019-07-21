from django.contrib import admin
from .models import Unidad, Receta, Ingrediente, Insumo  #importamos el modelo
# Register your models here.

admin.site.register(Unidad) # lo registramos
admin.site.register(Ingrediente) 
admin.site.register(Insumo) 
admin.site.register(Receta) 

#class ImageAdmin(admin.ModelAdmin):
    # explicitly reference fields to be shown, note image_tag is read-only
#    fields = ( 'imagen','externalURL', )
#    readonly_fields = ('image_tag',)
