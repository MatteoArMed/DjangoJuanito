from django.db import models

class Blog(models.Model):
    texto_descripcion = models.CharField(max_length=200)
    fecha_publicacion = models.DateTimeField("Fecha Publicación")
    def __str__(self):
        return self.texto_descripcion

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
    estado_correo = models.BooleanField(default=False)
    def __str__(self):
        return self.correo_contacto
    
class Servicios(models.Model):
    nombre_trabajo = models.CharField(max_length=255,blank=False,null=False)
    sub_titulo = models.CharField(max_length=255,blank=False,null=False)
    descripcion = models.TextField(max_length=1000,blank=False,null=False)
    precio = models.IntegerField(blank=False,null=False)
    imagen_trabajo = models.ImageField(upload_to="fotoservicios",null=True)
    def __str__(self):
        return self.nombre_trabajo
    