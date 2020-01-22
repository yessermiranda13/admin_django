import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Preguntas(models.Model):
    #atributos
    text_pregunta = models.CharField(max_length=200)
    fecha_pub = models.DateTimeField('fecha de publicacion')

    #métodos
    def __str__(self):
        return self.text_pregunta
    
    def publicaciones_recientes(self):
        return self.fecha_pub >= timezone.now() - datetime.timedelta(days=1)


class Eleccion(models.Model):
    #atributos
    pregunta = models.ForeignKey(Preguntas, on_delete=models.CASCADE)
    texto_seleccionado = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    #métodos
    def __str__(self):
        return self.texto_seleccionado