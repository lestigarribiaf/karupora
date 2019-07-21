from django.db import models
from django.contrib.auth.models import User

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
    def __str__(self):
        return self.nombre_receta
