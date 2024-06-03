from django.shortcuts import render
from .models import Deporte, Mensaje, Deportes2, Contenido, SubtituloE3

def index(request):
    mensajes = Mensaje.objects.all()
    deportes = Deporte.objects.all()
    return render(request, 'index.html', {'deportes': deportes, 'mensajes': mensajes})

def galeria(request):
    mensajes = Mensaje.objects.all()
    deportes2 = Deportes2.objects.all()
    
    return render(request, 'galeria.html', {'deportes2': deportes2, 'mensajes': mensajes})  
def contenido(request):
    mensajes = Mensaje.objects.all()
    contenido = Contenido.objects.all()
    subtituloE3 = SubtituloE3.objects.all()
    return render(request, 'contenido.html', {'contenido': contenido, 'mensajes': mensajes, 'subtituloE3': subtituloE3})
