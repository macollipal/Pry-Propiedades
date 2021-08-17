from django.shortcuts import render

# Create your views here.
from typing import Generic
from django.shortcuts import  render, redirect
from django.urls.base import reverse_lazy

from django.views import generic

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import  Riesgo
from .forms import  RiesgoForm


# Riesgo---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

class RiesgoView(LoginRequiredMixin, generic.ListView):
    model = Riesgo
    template_name = "risk/risk_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class RiesgoNew(LoginRequiredMixin, generic.CreateView):
    model = Riesgo
    template_name = "risk/risk_form.html"
    context_object_name = "obj"
    form_class = RiesgoForm
    success_url =reverse_lazy("risk:risk_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        return super().form_valid(form)

class RiesgoEdit(LoginRequiredMixin, generic.UpdateView):
    model = Riesgo
    template_name = "risk/risk_form.html"
    context_object_name = "obj"
    form_class = RiesgoForm
    success_url =reverse_lazy("risk:risk_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)
    
def riesgo_inactivar(request, id):
    riesgo = Riesgo.objects.filter(pk=id).first()
    contexto={}
    template_name="risk/risk_del.html"

    if not riesgo:
        return redirect("risk:risk_list")

    if request.method == 'GET':
        contexto = {'obj' :riesgo}
    
    if request.method == 'POST':
        riesgo.estado=False
        riesgo.save()
        return redirect("risk:risk_list")

    return render(request, template_name, contexto)