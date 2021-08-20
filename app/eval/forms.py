from django import forms
#from django.db import models
#from django.forms import fields, widgets
from .models import  Evaluacion, EvaluacionPeriodo, EvaluacionDet


#EVALUACION----------------------------------------------------------

class EvaluacionPeriodoForm(forms.ModelForm):
    fecha_eval =  forms.DateInput()

    class Meta:
        model = EvaluacionPeriodo
        
        #fields = ['codigo','codigo_barra','descripcion', 'estado', 'precio', 'existencia','ultima_compra', 'marca','subcategoria', 'u_medida']
        fields = ['fecha_eval']
        exclude =['created_date','modified_date','created_by' ,'modified_by', 'estado']
        #widget = {'observacion': forms.TextInput}
        #widget = {'fecha_eval': forms.DateInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        self.fields['fecha_eval'].widget.attrs['readonly'] = True
        #self.fields['ultima_compra'].widget.attrs['readonly'] = True
        #self.fields['existencia'].widget.attrs['readonly'] = True

class EvaluacionForm(forms.ModelForm):
    #fecha_eval =  forms.DateInput()

    class Meta:
        model = Evaluacion
        
        #fields = ['codigo','codigo_barra','descripcion', 'estado', 'precio', 'existencia','ultima_compra', 'marca','subcategoria', 'u_medida']
        fields = ['fecha_eval','observacion' ]
        exclude =['created_date','modified_date','created_by' ,'modified_by', 'estado']
        #widget = {'observacion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        #self.fields['fecha_eval'].widget.attrs['readonly'] = True
        #self.fields['ultima_compra'].widget.attrs['readonly'] = True
        #self.fields['existencia'].widget.attrs['readonly'] = True

class EvaluacionDetalleForm(forms.ModelForm):
    #fecha_eval =  forms.DateInput()

    class Meta:
        model = EvaluacionDet
        
        #fields = ['codigo','codigo_barra','descripcion', 'estado', 'precio', 'existencia','ultima_compra', 'marca','subcategoria', 'u_medida']
        fields = ['evaluacion','propiedad','riesgo' ]
        exclude =['created_date','modified_date','created_by' ,'modified_by', 'estado']
        #widget = {'observacion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        #self.fields['fecha_eval'].widget.attrs['readonly'] = True
        #self.fields['ultima_compra'].widget.attrs['readonly'] = True
        #self.fields['existencia'].widget.attrs['readonly'] = True