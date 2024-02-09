
from django.urls import path

from .views import home, contacto, servicios, gasfiteria, fozaseptica, obrasmenores, quienesomos

urlpatterns = [
    path("", home, name="home"),
    path("contacto",contacto, name="contacto"),
    path("servicios",servicios, name="servicios"),
    path("gasfiteria",gasfiteria, name="gasfiteria"),
    path("fozaseptica",fozaseptica, name="fozaseptica"),
    path("obrasmenores",obrasmenores, name="obrasmenores"),
    path("quienesomos",quienesomos, name="quienesomos"),

]