
from django.urls import path
from .views import home, contacto, servicios, gasfiteria, fosaseptica, obrasmenores, quienesomos, addservicio,eliminarServicio,mensajeRespuesta,mensajeRespuestaComun,correoLeido,correoNoLeido,modificarServicio,login



urlpatterns = [
    path("", home, name="home"),
    path("contacto",contacto, name="contacto"),
    path("accounts/login/",login,name="login"),
    path("servicios",servicios, name="servicios"),
    path("gasfiteria",gasfiteria, name="gasfiteria"),
    path("fosa",fosaseptica, name="fosaseptica"),
    path("obrasmenores",obrasmenores, name="obrasmenores"),
    path("quienesomos",quienesomos, name="quienesomos"),
    path("addservicio",addservicio,name="addservicio"),
    path('eliminarServicio/<str:pk>/',eliminarServicio, name='eliminarServicio'),
    path('mensajeRespuesta',mensajeRespuesta,name='mensaje'),
    path('mensajeRespuestaComun',mensajeRespuestaComun,name='mensajeComun'),
    path('correoLeido/<int:pk>/',correoLeido,name='correoLeido'),
    path('correoNoLeido/<int:pk>/',correoNoLeido,name='correoNoLeido'),
    path('modificar/<int:pk>/',modificarServicio,name='modificar'),
]

