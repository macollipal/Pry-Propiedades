from django.urls import path


from .views import EvalView, evaluaciones_fct,  evaluacion_inactivar
    

urlpatterns = [

    path('evaluaciones/' , EvalView.as_view(), name='eval_list'),
    path('evaluaciones/new' , evaluaciones_fct, name='eval_new'),
    path('evaluaciones/edit/<int:evaluacion_id>' , evaluaciones_fct , name='eval_edit'),
    path('evaluaciones/inactivar/<int:id>' , evaluacion_inactivar, name='evaluacion_inactivar'),

    
]
