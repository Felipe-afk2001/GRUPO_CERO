from core.models import obras
from django.shortcuts import redirect, render
from .forms import modificar_form, obras_form

# Create your views here.
def subir (request):
    msg1= ''
    formulario= obras_form()
    if request.method == 'POST':
        formulario=obras_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            msg1='la obra se ha subido correctamente'
        else:
            msg3='la obra ya existe'
    contexto = {
        'formulario':formulario, 'msg1':msg1
    }
    return render(request,'adminapp/subir.html',contexto)

def modificar (request, id):
    msg2= ''
    Obra=obras.objects.get(id_obra=id)
    formulario2= modificar_form()
    if request.method == 'POST':
        formulario2=modificar_form(request.POST)
        if formulario2.is_valid():
            formulario2.save()
            msg2='la obra se ha modificado correctamente'
        else:
            msg3='Error'
    contexto = {
        'formulario2':formulario2, 'msg2':msg2, 'Obra':Obra
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
    return redirect(to="mostrar")

