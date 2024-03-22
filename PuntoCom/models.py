from django.db import models
from django.db.models.functions import Now
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
    

class Contacto(models.Model):
    correo_contacto = models.EmailField(max_length=100,blank=False,null=False)
    tipo_trabajo = models.CharField(max_length=100)
    descripcion_trabajo = models.TextField(blank=True)
    fecha_contacto = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.correo_contacto
    
class Servicios(models.Model):
    nombre_trabajo = models.CharField(max_length=255,blank=False,null=False)
    sub_titulo = models.CharField(max_length=255,blank=False,null=False)
    descripcion = models.TextField(max_length=1000,blank=False,null=False)
    precio = models.IntegerField(max_length=11,blank=False,null=False)
    def __str__(self):
        return self.nombre_trabajo