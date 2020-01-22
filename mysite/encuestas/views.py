from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from .models import Preguntas
from django.template import loader

#def index(request):
 #   lista_preguntas_recientes = Preguntas.objects.order_by('-fecha_pub')[:5]
  #  plantilla = loader.get_template('encuestas/index.html')
   # context = {
    #    'lista_preguntas_recientes': lista_preguntas_recientes,
    #}
    #return HttpResponse(plantilla.render(context, request))
def index(request):
    lista_preguntas_recientes = Preguntas.objects.order_by('-fecha_pub')[:5]
    context = {'lista_preguntas_recientes': lista_preguntas_recientes}
    return render(request, 'encuestas/index.html', context)

def detalle(request, id_pregunta):
    try:
        pregunta = Preguntas.objects.get(pk=id_pregunta)
    except Preguntas.DoesNotExist:
        raise Http404("Pregunta inexistente")
    return render(request, 'encuestas/detalle.html', {'pregunta': pregunta})
    #return HttpResponse("Tu estas viendo la pregunta %s." %id_pregunta)

def resultados(request, id_pregunta):
    response = "Estas viendo los resultados de la pregunta %s."
    return HttpResponse(response % id_pregunta)

def voto(request, id_pregunta):
    return HttpResponse("estas votando por la pregunta %s." %id_pregunta)