# models.py en PortafolioApp

from django.db import models
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='categorias/', null=True, blank=True)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    imagen = models.ImageField(upload_to='noticias', null=True, blank=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Ejemplo de asignación a una Categoria existente

    def __str__(self):
        return self.titulo
