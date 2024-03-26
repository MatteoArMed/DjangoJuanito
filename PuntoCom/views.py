from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import TemplateSyntaxError
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
        obj.save()
        print('Datos guardados')
        return render(request,'mensajes.html',context)
    


def eliminarServicio(request,pk):
    context = {}
    try:
        servicios = Servicios.objects.get(id=pk)
        servicios.delete()
        print("Servicio eliminado")
        servicio = Servicios.objects.all()
        context = {'mensaje':'Servicio eliminado','servicios':servicio}
        return render(request,'mensajes.html',context)
    except:
        servicios = Servicios.objects.all()
        context = {'mensaje':'Servicio no existe','servicios':servicios}
        return render(request,'addservicios.html',context)

def mensajeRespuesta(request):
    if request.method != 'POST':
        context = {'mensaje':'Esto es un mensaje'}
        return render(request,'mensajeRespuesta',context)

def format_precio(precio):
    try:
        precio_sin_decimales = int(precio / 100)
        precio_formateado = f"{precio_sin_decimales:.0f}"  # Eliminar decimales y usar punto
        return f"${precio_formateado}"  # Agregar símbolo de pesos
    except ValueError:
        raise TemplateSyntaxError("Precio no es un número válido")
    
# @login_required
# def eliminarTrabajo(request,pk):
#     context = {}
#     try:
#         trabajo = Atencion.objects.get(id=pk)

#         trabajo.delete()
#         print('Trabajo Eliminado')
#         trabajos =  Atencion.objects.all()
#         context ={'mensaje':'Trabajo Eliminado', 'trabajos':trabajos}
#         return render(request,'mecanico/datosContacto.html',context)
#     except:
#         trabajos =  Atencion.objects.all()
#         context={'mensaje':'El trabajo no existe','trabajos':trabajos}
#         return render(request,'mecanico/administrarTrabajos.html',context)