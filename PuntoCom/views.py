from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .models import Contacto, Servicios


def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method != "POST":
        context = {'mensaje': 'Ingresa tus credenciales'}
        return render(request, 'registration/login.html',context)
    else:
        usuario = request.POST["usuario"]
        contrasenna = request.POST["contrasenna"]

        user = authenticate(request, username=usuario, password=contrasenna)
        if user is not None:
            auth_login(request,user)
            return redirect('home')
        else:
            context = {'mensaje':'Usuario o contraseña incorrectas'}
            return render(request,'registration/login.html',context)



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
        return render(request, 'mensajecomun.html',context)

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

@login_required
def addservicio(request):
    contactos = Contacto.objects.all() #Traemos todos los mensajes de contacto
    # servicios = Servicios.objects.all() #Traemos todos los servicios disponibles
    servicios = Servicios.objects.filter(estado_trabajo=True) #Traemos todos los servicios disponibles
    correosleidos = Contacto.objects.filter(estado_correo=True) #Traemos los coreros leidos
    correosnoleidos = Contacto.objects.filter(estado_correo=False) #Traemos los coreros no leidos


    context = {
        'contactos': contactos,
        'servicios': servicios,
        'correoleido': correosleidos,
        'correonoleido': correosnoleidos,
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
        context = {
            'mensaje':'Trabajo creado'
        }
        return render(request,'mensajes.html',context)
    
def error(request):
    return render(request,'mensajeRespuestaComun')


def eliminarServicio(request,pk):
    # if pk != "":
    #     servicio = Servicios.objects.get(id=pk)
    #     context = {'servicio': servicio}
    
    # if request.method != "POST":
    #     return render(request,'modificarServicio.html',context)

    # if request.method == "POST":
    #     servicio.estado_trabajo = False
    #     servicio.save()
    #     context = {'mensaje':'Trabajo modificado'}
    #     print('Se envian datos')
    #     return render(request, 'mensajes.html',context)
    
    context = {}
    try:
        servicios = Servicios.objects.get(id=pk)
        servicios.estado_trabajo = False
        servicios.save()
        print("Servicio eliminado")
        servicio = Servicios.objects.all()
        context = {'mensaje':'Trabajo eliminado','servicios':servicio}
        return render(request,'mensajes.html',context)
    except:
        servicios = Servicios.objects.all()
        context = {'mensaje':'Trabajo no existe','servicios':servicios}
        return render(request,'addservicios.html',context)





def mensajeRespuesta(request):
    if request.method != 'POST':
        context = {'mensaje':'Esto es un mensaje'}
        return render(request,'mensajeRespuesta',context)

def mensajeRespuestaComun(request):
    if request.method != 'POST':
        context = {'mensaje':'Esto es un mensaje'}
        return render(request,'mensajeRespuestaComun',context)


def correoLeido(request, pk):
    if pk != "":
        correosnoleidos = Contacto.objects.get(id=pk)
        context = {'mensaje': ''}

        if request.method != "POST":
            context = {'mensaje': 'Cargando pagina'}
            print('No es metodo POST')
            return render(request,'mensajes.html',context)
        else:
            cambioestado = request.POST["cambioEstado"]
            correosnoleidos.estado_correo = cambioestado
            correosnoleidos.save()

            context = {'mensaje': 'Correo leido'}
            print('Se cambia el estado del correo')
            return render(request, 'mensajes.html',context)

def correoNoLeido(request, pk):
    if pk != "":
        correoleido = Contacto.objects.get(id=pk)
        context = {'mensaje': ''}

        if request.method != "POST":
            context = {'mensaje':'No es metodo POST'}
            return render(request,'mensajes.html',context)
        else:
            cambioestado = request.POST["correoNoLeido"]
            correoleido.estado_correo = cambioestado
            correoleido.save()

            context = {'mensaje':'Se cambia a correo no leido'}
            return render(request,'mensajes.html',context)

@login_required
def modificarServicio(request, pk):
    if pk != "":
        servicio = Servicios.objects.get(id=pk)
        context = {'servicio': servicio}

        if request.method != "POST":
            return render (request,'modificarServicio.html',context)

        if request.method == "POST":
            nombreServicio = request.POST["nombreServicio"]
            subtituloServicio = request.POST["subtitulo"]
            descripcionServicio = request.POST["descripcionServicio"]
            precioServicio = request.POST["precioservicio"]
            
            # validamos si se sube una imagen, si no se conserva la que tiene
            if 'imagenServicio' in request.FILES:
                imagenServicio = request.FILES["imagenServicio"]
                servicio.imagen_trabajo = imagenServicio
            
            servicio.nombre_trabajo = nombreServicio
            servicio.sub_titulo = subtituloServicio
            servicio.descripcion = descripcionServicio
            servicio.precio = precioServicio
            servicio.save()

            context = {'mensaje':'Trabajo modificado'}
            print('Se envian datos')
            return render(request, 'mensajes.html',context)

        else:
            context = {'mensaje': 'Error, el trabajo no existe...'}
            return render(request,'mensajes.html',context)
