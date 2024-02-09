from django.db import models

# from django.utils import timezone

# Create your models here.

class Blog(models.Model):
    texto_descripcion = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField("Fecha Publicación")
    def __str__(self):
        return self.texto_descripcion
    # def publicacion_hecho_reciente(self):
    #     return self.fecha_publicacion >= timezone.now() - datetime.timedelta(days=1)


class Trabajos(models.Model):
    lugar_trabajo = models.CharField(max_length=200)
    descripcion_trabajo = models.CharField(max_length=1000)
    tipo_trabajo = models.CharField(max_length=200)
    def __str__(self):
        return self.lugar_trabajo
    

