from django.urls import path


from .views import PropiedadView, PropiedadNew, PropiedadEdit, propiedad_inactivar
    

urlpatterns = [

    path('propiedad/' , PropiedadView.as_view(), name='propiedad_list'),
    path('propiedad/new' , PropiedadNew.as_view(), name='propiedad_new'),
    path('propiedad/edit/<int:pk>' , PropiedadEdit.as_view(), name='propiedad_edit'),
    path('propiedad/inactivar/<int:id>' , propiedad_inactivar, name='propiedad_inactivar'),

    
]
