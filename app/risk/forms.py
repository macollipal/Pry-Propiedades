from django import forms
#from django.db import models
#from django.forms import fields, widgets
from .models import  Riesgo


#PROPIEDAD----------------------------------------------------------

class RiesgoForm(forms.ModelForm):
    class Meta:
        model = Riesgo
        #fields = ['codigo','codigo_barra','descripcion', 'estado', 'precio', 'existencia','ultima_compra', 'marca','subcategoria', 'u_medida']
        fields = ['codigo','tipo','nombre', 'valor','estado']
        exclude =['created_date','modified_date','created_by' ,'modified_by']
        widget = {'nombre': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class':'form-control'
            })
        #self.fields['ultima_compra'].widget.attrs['readonly'] = True
        #self.fields['existencia'].widget.attrs['readonly'] = True
