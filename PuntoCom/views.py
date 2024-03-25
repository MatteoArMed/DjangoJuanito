from django.http import HttpResponseRedirect
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

def addservicio(request):
    contactos = Contacto.objects.all() #Traemos todos los mensajes de contacto
    servicios = Servicios.objects.all() #Traemos todos los servicios disponibles
    context = {
        'contactos': contactos,
        'servicios': servicios
    }
    if request.method != "POST":
        return render(request,'addservicios.html',context)
        
    else:
        nombreServicio = request.POST["nombreServicio"]
        subTitulo = request.POST["subTitulo"]
        descripcionServicio = request.POST["descripcionServicio"]
        precioServicio = request.POST["precioServicio"]
        imagen = request.FILES["fotosServicio"]
        
        def siguienteID():
            ultimoServicio = Servicios.objects.order_by('-id').first()
            if ultimoServicio:
                return ultimoServicio.id + 1
            else:
                return 1

        obj = Servicios.objects.create(
            id = siguienteID(),
            nombre_trabajo = nombreServicio,
            sub_titulo = subTitulo,
            descripcion = descripcionServicio,
            precio = precioServicio,
            imagen_trabajo = imagen
        )
        print('Datos guardados')
        return render(request,'addservicios.html',context)

