from django.urls import path


from .views import RiesgoView, RiesgoNew, RiesgoEdit, riesgo_inactivar
    

urlpatterns = [

    path('riesgo/' , RiesgoView.as_view(), name='riesgo_list'),
    path('riesgo/new' , RiesgoNew.as_view(), name='riesgo_new'),
    path('riesgo/edit/<int:pk>' , RiesgoEdit.as_view(), name='riesgo_edit'),
    path('riesgo/inactivar/<int:id>' , riesgo_inactivar, name='riesgo_inactivar'),

    
]
