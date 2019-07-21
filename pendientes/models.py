from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from django.conf import settings

MEDIA_ROOT = 'C:/Users/Admin/Desktop/karupora/pendientes/static/img'
MEDIA_URL = '/static/img'
# Create your models here.

class Unidad(models.Model):
    nombre_unidad = models.CharField(max_length=100)
    siglas_unidad = models.CharField(max_length=10)
    def __str__(self):
        return self.nombre_unidad

class Ingrediente(models.Model):
    nombre_ingredientes = models.CharField(max_length=100)
    unidad = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre_ingredientes

class Insumo(models.Model):
    ingrediente_insumo = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad_insumo = models.FloatField()
    def __str__(self):
        return self.ingrediente_insumo.nombre_ingredientes + " - " + str(self.cantidad_insumo) + " " + str(self.ingrediente_insumo.unidad.siglas_unidad)

class Receta(models.Model):
    nombre_receta = models.CharField(max_length=100)
    porciones = models.IntegerField(null=True, blank=True)
    insumos = models.ManyToManyField(Insumo)
   # imagen = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
   # externalURL = models.URLField(blank=True)
    
   # def url(self):
        # returns a URL for either internal stored or external image url
   #     if self.externalURL:
    #        return self.externalURL
     #   else:
            # is this the best way to do this??
      #      return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.imagen)))

    #def image_tag(self):
        # used in the admin site model as a "thumbnail"
   #     return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()) )
   # image_tag.short_description = 'Recetas'    

    def __str__(self):
        return self.nombre_receta
