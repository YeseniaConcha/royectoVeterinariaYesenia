from django.db import models

# Create your models here.

class Veterinaria(models.Model):
    nombre = models.CharField(max_length=100)
    FechaAtencion = models.CharField(max_length=100)
    motivo = models.CharField(max_length=100)
    diagnostico = models.CharField(max_length=100)
    tratamiento = models.CharField(max_length=100)
    observacion = models.CharField(max_length=100)
    valor = models.IntegerField()

    def __str__(self) -> str:
        return self.nombre

# class Dueños(models.Model):
#     nombre = models.CharField(max_length=100)
#     edad = models.IntegerField()

