from enum import unique
from django.db import models

from bases.models import ClaseModelo


class Riesgo(ClaseModelo):
    codigo= models.CharField(max_length=20, unique=True)
    tipo = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    valor = models.FloatField(default=0)
    


    def __str__(self) :
        return '{}'.format(self.nombre)

    def save(self):
        self.descripcion = self.nombre.upper()
        super(Riesgo, self).save()

    class Meta:
        verbose_name_plural="Riesgos"
        unique_together =('codigo', 'tipo')

