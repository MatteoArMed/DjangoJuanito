from django.shortcuts import render, redirect
from .models import Contacto, Servicios


def home(request):
    return render(request, 'home.html')


def contacto(request):
    if request.method != "POST":
        context = {'mensaje': '¿Que quieres hacer?'}
        return render(request,'contacto.html',context)
    else:
        email = request.POST["email"]
        tipoTrabajo = request.POST["tipotrabajo"]
        descripcion = request.POST["descripcion"]

        obj = Contacto.objects.create(
            correo_contacto = email,
            tipo_trabajo = tipoTrabajo,
            descripcion_trabajo = descripcion)
        print('Datos guardados')
        context = {'mensaje':'Formulario enviado, pronto nos pondremos en contacto contigo.'}
        return render(request, 'contacto.html',context)



def servicios(request):
    return render(request,'servicios.html')

def gasfiteria(request):
    return render(request, 'gasfiteria.html')

def fosaseptica(request):
    return render(request, 'fosaseptica.html')

def obrasmenores(request):
    return render(request, 'obrasmenores.html')

def quienesomos(request):
    return render(request, 'quienesomos.html')

# def agregarservicio(request):
#     if request.method != "POST":
#         context = {'mensaje':'Aqui debes subir una imagen referencial'}
#         return (request,'addservicios.html')
#     else:
        
def addservicio(request):
    contactos = Contacto.objects.all() #Traemos todos los mensajes de contacto
    servicios = Servicios.objects.all() #Traemos todos los servicios disponibles
    context = {
        'contactos': contactos,
        'servicios': servicios
    }
    return render(request,'addservicios.html',context)