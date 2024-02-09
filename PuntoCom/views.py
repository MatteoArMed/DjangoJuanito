from django.shortcuts import render, redirect 


# Create your views here.
from django.http import HttpResponse

def home(request):
    # Lógica de tu vista...
    imagen_url = ''  # Ruta relativa a tus archivos estáticos en S3
    return render(request, 'home.html', {'imagen_url': imagen_url})

# def home(request):
#     return render(request, 'home.html')

def contacto(request):
    return render(request,'contacto.html')

def servicios(request):
    return render(request,'servicios.html')

def gasfiteria(request):
    return render(request, 'gasfiteria.html')

def fozaseptica(request):
    return render(request, 'fozaseptica.html')

def obrasmenores(request):
    return render(request, 'obrasmenores.html')

def quienesomos(request):
    return render(request, 'quienesomos.html')