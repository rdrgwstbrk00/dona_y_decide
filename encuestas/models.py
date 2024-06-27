from django.db import models
from django.db.models import Avg

class Encuesta(models.Model):
    id_encuesta = models.AutoField(primary_key=True)
    texto_encuesta = models.CharField(max_length=255)
    activa = models.BooleanField(default=True)

    def __str__(self):
        return self.texto_encuesta

class ResultadoEncuesta(models.Model):
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE)
    respuesta = models.IntegerField(choices=[(i, str(i)) for i in range(1, 8)], default=1)
    imagen_respuesta = models.ImageField(upload_to='imagenes_respuestas/', blank=True, null=True)

    def __str__(self):
        return f"{self.encuesta} - {self.respuesta}"

def calcular_promedio_encuesta(encuesta):
    promedio = ResultadoEncuesta.objects.filter(encuesta=encuesta).aggregate(promedio=Avg('respuesta'))['promedio']
    return promedio


class ProductoDonado(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    calificacion = models.IntegerField()
    imagen = models.ImageField(upload_to='productos_imagenes/', blank=True, null=True)

    def __str__(self):
        return self.nombre