from django.contrib import admin

from .models import Blog, Trabajos, Servicios, Contacto
# Register your models here.

admin.site.register(Contacto)
admin.site.register(Trabajos)
admin.site.register(Servicios)
admin.site.register(Blog)
