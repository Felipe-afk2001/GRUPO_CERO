from django.db import models
from .models import autor
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'core/index.html')
def obras(request):
    return render(request,'core/obras.html')
def autores(request):
    
    autores=autor.objects.all()
    contexto={
        'autores':autores
    }
    return render(request,'core/autores.html',contexto)