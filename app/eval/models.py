
from django.db import models

#Para los signals
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum

from bases.models import ClaseModelo
from prop.models import Propiedad

class EvaluacionPeriodo(ClaseModelo):
    fecha_eval=models.DateField(null=True,blank=True)

    def __str__(self) :
        return '{}'.format(self.fecha_eval)

    def save(self):
        #self.descripcion = self.fecha_eval.upper()
        super(EvaluacionPeriodo, self).save()

    class Meta:
        verbose_name_plural="Evaluacion_Periodos"
        #unique_together =('codigo', 'tipo')


class Evaluacion(ClaseModelo):
    fecha_eval=models.ForeignKey(EvaluacionPeriodo,on_delete=models.CASCADE)
    observacion=models.TextField(blank=True,null=True)
    #no_factura=models.CharField(max_length=100)
    #fecha_factura=models.DateField()
    #sub_total=models.FloatField(default=0)
    #descuento=models.FloatField(default=0)
    #total=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        #if self.sub_total == None  or self.descuento == None:
        #    self.sub_total = 0
        #    self.descuento = 0
            
        #self.total = self.sub_total - self.descuento
        
        super(Evaluacion,self).save()

    class Meta:
        verbose_name_plural = "Evaluaciones"
        verbose_name="Evaluacion"

class EvaluacionDet(ClaseModelo):
    evaluacion=models.ForeignKey(Evaluacion,on_delete=models.CASCADE)
    propiedad=models.ForeignKey(Propiedad,on_delete=models.CASCADE)
    riesgo=models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.evaluacion)

    def save(self):
    #    self.riesgo = self.riesgo.upper()
        #if self.sub_total == None  or self.descuento == None:
        #    self.sub_total = 0
        #    self.descuento = 0
            
        #self.riesgo = self.riesgo
        
        super(EvaluacionDet,self).save()

    class Meta:
        verbose_name_plural = "EvaluacionesDetalles"
        verbose_name="EvaluacionDetalle"