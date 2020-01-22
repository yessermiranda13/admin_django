from django.urls import path

from . import views

urlpatterns = [
    #ex: /encuestas/
    path('', views.index, name='index'),
    #ex: /encuestas/5/
    path('<int:id_pregunta>/',views.detalle, name='detalle'),
    #ex: /encuestas/5/resultados/
    path('<int:id_pregunta>/resultados',views.resultados,name='resultados'),
    #ex: /encuestas/5/voto/
    path('<int:id_pregunta>/voto/',views.voto, name='voto'),
]