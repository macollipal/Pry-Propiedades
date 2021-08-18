from django.urls import path


from .views import EvalView, evaluaciones_fct,  evaluacion_inactivar, \
     EvalPerView, EvalPerNew ,EvalPerEdit, evaluacion_per_inactivar
    

urlpatterns = [
    

    path('eval_periodo/' , EvalPerView.as_view(), name='eval_per_list'),
    path('eval_periodo/new' , EvalPerNew.as_view(), name='eval_per_new'),
    #path('propiedad/edit/<int:pk>' , PropiedadEdit.as_view(), name='propiedad_edit'),
    path('eval_periodo/edit/<int:pk>' , EvalPerEdit.as_view(), name='eval_per_edit'),
    path('eval_periodo/inactivar/<int:id>' , evaluacion_per_inactivar, name='evaluacion_per_inactivar'),

    path('evaluaciones/' , EvalView.as_view(), name='eval_list'),
    path('evaluaciones/new' , evaluaciones_fct, name='eval_new'),
    path('evaluaciones/edit/<int:evaluacion_id>' , evaluaciones_fct , name='eval_edit'),
    path('evaluaciones/inactivar/<int:id>' , evaluacion_inactivar, name='evaluacion_inactivar'),

    
]
