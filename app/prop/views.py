from typing import Generic
from django.shortcuts import  render, redirect
from django.urls.base import reverse_lazy

from django.views import generic

# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin


from .models import  Propiedad
from .forms import  PropiedadForm


# PropiedadES---------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------

class PropiedadView(LoginRequiredMixin, generic.ListView):
    model = Propiedad
    template_name = "prop/propiedad_list.html"
    context_object_name = "obj"
    login_url = 'bases:login'

class PropiedadNew(LoginRequiredMixin, generic.CreateView):
    model = Propiedad
    template_name = "prop/propiedad_form.html"
    context_object_name = "obj"
    form_class = PropiedadForm
    success_url =reverse_lazy("prop:propiedad_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.created_by = self.request.user 
        return super().form_valid(form)

class PropiedadEdit(LoginRequiredMixin, generic.UpdateView):
    model = Propiedad
    template_name = "prop/propiedad_form.html"
    context_object_name = "obj"
    form_class = PropiedadForm
    success_url =reverse_lazy("prop:propiedad_list")
    login_url = 'bases:login'

    def form_valid(self, form):
        form.instance.modified_by = self.request.user.id
        return super().form_valid(form)
    
def propiedad_inactivar(request, id):
    propiedad = Propiedad.objects.filter(pk=id).first()
    contexto={}
    template_name="prop/propiedad_del.html"

    if not propiedad:
        return redirect("prop:propiedad_list")

    if request.method == 'GET':
        contexto = {'obj' :propiedad}
    
    if request.method == 'POST':
        propiedad.estado=False
        propiedad.save()
        return redirect("prop:propiedad_list")

    return render(request, template_name, contexto)