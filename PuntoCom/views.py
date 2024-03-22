from django.shortcuts import render, redirect 
from .models import Contacto

# Create your views here.
from django.http import HttpResponse

def home(request):
    # Lógica de tu vista...
    imagen_url = ''  # Ruta relativa a tus archivos estáticos en S3
    return render(request, 'home.html', {'imagen_url': imagen_url})

# def home(request):
#     return render(request, 'home.html')

def contacto(request):
    if request.method != "POST":
        context = {'mensaje': 'no es POST'}
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
        context = {'mensaje':'Formulario enviado'}
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