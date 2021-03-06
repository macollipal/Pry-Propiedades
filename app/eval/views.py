
from django.shortcuts import render, redirect
from typing import Generic
from django.shortcuts import render, redirect
from django.urls.base import reverse_lazy
import datetime
from django.http import HttpResponse

from django.views import generic

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import EvaluacionPeriodo, Evaluacion, EvaluacionDet

from prop.models import Propiedad

from eval.forms import EvaluacionPeriodoForm, EvaluacionForm,  EvaluacionDetalleForm


class EvalPerView(LoginRequiredMixin, generic.ListView):
    model = EvaluacionPeriodo
    template_name = "eval/eval_per_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'


class EvalPerNew(LoginRequiredMixin, generic.CreateView):
    model = EvaluacionPeriodo
    template_name = "eval/eval_per_form.html"
    context_object_name = "obj"
    form_class = EvaluacionPeriodoForm
    success_url = reverse_lazy("eval:eval_per_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class EvalPerEdit(LoginRequiredMixin, generic.UpdateView):
    model = EvaluacionPeriodo
    template_name = "eval/eval_per_form.html"
    context_object_name = "obj"
    print("aqi")
    form_class = EvaluacionPeriodoForm
    success_url =reverse_lazy("eval:eval_per_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)

        

def evaluacion_per_inactivar(request, id):
    evaluacionper = EvaluacionPeriodo.objects.filter(pk=id).first()
    contexto = {}
    template_name = "eval/eval_del.html"

    if not evaluacionper:
        return redirect("eval:eval_per_list")

    if request.method == 'GET':
        contexto = {'obj': evaluacionper}

    if request.method == 'POST':
        evaluacionper.estado = False
        evaluacionper.save()
        return redirect("eval:eval_per_list")

    return render(request, template_name, contexto)


# EVALUACIONES---------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------

class EvalView(LoginRequiredMixin, generic.ListView):
    model = Evaluacion
    template_name = "eval/eval_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'



def evaluacion_inactivar(request, id):
    evaluacion = Evaluacion.objects.filter(pk=id).first()
    contexto = {}
    template_name = "eval/eval_del.html"

    if not evaluacion:
        return redirect("eval:eval_list")

    if request.method == 'GET':
        contexto = {'obj': evaluacion}

    if request.method == 'POST':
        evaluacion.estado = False
        evaluacion.save()
        return redirect("eval:eval_list")

    return render(request, template_name, contexto)


# --------------------------------------------------------Vista basada en funciones

def evaluaciones_fct(request, evaluacion_id=None):
    template_name = "eval/eval_form.html"
    obj_prop = Propiedad.objects.filter(estado=True)
    form_eval = {}
    form_detalle ={}
    contexto = {}
#GET-------------------------------------------------------------------------------------------
    if request.method == 'GET':
        form_eval = EvaluacionForm()
        form_detalle =EvaluacionDetalleForm()

        enc = Evaluacion.objects.filter(pk=evaluacion_id).first()
        #det= EvaluacionDet.objects.filter(pk=evaluacion_id).first()

        if enc:
            det = EvaluacionDet.objects.filter(evaluacion=enc.pk)
            #fecha_eval = datetime.date.isoformat(enc.fecha_eval)
            fecha_eval = enc.fecha_eval
            e = {
                'fecha_eval': fecha_eval,
                'observacion': enc.observacion
            }

            form_eval = EvaluacionForm(e)

            #form_detalle = EvaluacionDetalleForm(det)
        else:
            det = None

        contexto = {'propiedad':obj_prop,'encabezado': enc, 'detalle':det, 'form_enc': form_eval}
#POST-------------------------------------------------------------------------------------------
    if request.method == 'POST':
        fecha_eval = request.POST.get("fecha_eval")
        observacion = request.POST.get("observacion")

        
        direccion = request.POST.get("direccion")
        riesgo = request.POST.get("riesgo")
    
#-------Guardar
        if not evaluacion_id:
            evaper  =EvaluacionPeriodo.objects.get(pk=fecha_eval)

            enc = Evaluacion(
                fecha_eval = evaper,
                observacion = observacion,
                created_by = request.user
            )
            
            det = EvaluacionDet(
                evaluacion_id =2,
                propiedad_id = 1,
                riesgo= 1,
                created_by = request.user
            )

            
            
            if enc:
                enc.save()
                evaluacion_id = enc.id
            
            if det:
                det.save()
                #evaluacion_id = enc.id
#-------Actualizar        
        else:
            evaper  =EvaluacionPeriodo.objects.get(pk=fecha_eval)
            enc = Evaluacion.objects.filter(pk=evaluacion_id).first()

            if enc:
                enc.fecha_eval = evaper
                enc.observacion = observacion
                enc.modified_by = request.user.id
                enc.save()

        return redirect("eval:eval_list")
        # if not evaluacion_id:
        # return redirect("eval:eval_list")

        # return redirect("eval:eval_edit",evaluacion_id=evaluacion_id)

    return render(request, template_name, contexto)
