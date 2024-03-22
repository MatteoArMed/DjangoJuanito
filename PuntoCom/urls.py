
from django.urls import path
from .views import home, contacto, servicios, gasfiteria, fosaseptica, obrasmenores, quienesomos, addservicio

urlpatterns = [
    path("", home, name="home"),
    path("contacto",contacto, name="contacto"),
    path("servicios",servicios, name="servicios"),
    path("gasfiteria",gasfiteria, name="gasfiteria"),
    path("fosa",fosaseptica, name="fosaseptica"),
    path("obrasmenores",obrasmenores, name="obrasmenores"),
    path("quienesomos",quienesomos, name="quienesomos"),
    path("addservicio",addservicio,name="addservicio"),
]

