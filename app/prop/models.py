from enum import unique
from django.db import models

from bases.models import ClaseModelo


#PROPIEDAD        

class Propiedad(ClaseModelo):
    codigo= models.CharField(max_length=20, unique=True)
    direccion = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    comuna = models.CharField(max_length=200, null=True)
    latitud = models.CharField(max_length=200,null=True)
    longitud = models.CharField(max_length=200,null=True)
    #uf = models.FloatField(default=0)
    #existencia = models.IntegerField(default=0)
    #ultima_compra = models.DateField(null=True, blank=True)

    #marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    #u_medida = models.ForeignKey(UM, on_delete=models.CASCADE)
    #subcategoria = models.ForeignKey(SubCategoria, on_delete=models.CASCADE)

    def __str__(self) :
        return '{}'.format(self.direccion)

    def save(self):
        self.descripcion = self.direccion.upper()
        super(Propiedad, self).save()

    class Meta:
        verbose_name_plural="Propiedades"
        #unique_together =('codigo')