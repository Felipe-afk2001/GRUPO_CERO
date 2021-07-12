from django.db import models
from .models import autor
from .models import obras as Obras
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')
def obras(request,id):
    obra=Obras.objects.get(id_obra=id)
    contexto = {
        'obra':obra
    }
    return render(request,'core/obras.html',contexto)
def autores(request):
    autores=autor.objects.all()
    contexto={
        'autores':autores
    }
    return render(request,'core/autores.html',contexto)
def login(request):
    return render(request,'core/Iniciar_sesion.html')

def chicagogaleria(request):
    return render(request,'core/chicagogaleria.html')
def Autor(request,id):
    obra=Obras.objects.filter(autor=id)
    Autor=autor.objects.get(id_autor=id)
    contexto={
        'autor':Autor,
        'obras':obra
    }
    return render(request,'core/autor.html',contexto)  