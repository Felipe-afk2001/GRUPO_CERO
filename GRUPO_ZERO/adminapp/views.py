from core.models import obras
from django.shortcuts import redirect, render
from .forms import modificar_form, obras_form, borrar_form

# Create your views here.
def subir (request):
    msg1= ''
    formulario= obras_form()
    if request.method == 'POST':
        formulario=obras_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            msg1='la obra se ha subido correctamente'

    contexto = {
        'formulario':formulario, 'msg1':msg1
    }
    return render(request,'adminapp/subir.html',contexto)

def modificar (request, id):
    obra=obras.objects.get(id_obra=id)
    formulario= obras_form()
    contexto={
        'form':modificar_form(instance=obra)
    }
    return render(request,'adminapp/modificar.html',contexto)

def mostrar (request):
    obra=obras.objects.all()
    contexto={
        'obra':obra
    }
    return render(request,'adminapp/mostrar.html',contexto)

def eliminar (request,id):
        obra=obras.objects.get(id_obra=id)
        obra.delete()
    return render(request, 'mostrar')

