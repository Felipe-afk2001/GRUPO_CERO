from django.shortcuts import redirect, render
from .forms import obras_form

# Create your views here.
def subir (request):
    msg= ''
    formulario= obras_form()
    if request.method == 'POST':
        formulario=obras_form(request.POST)
        if formulario.is_valid():
            formulario.save()
            msg='la obra se ha subido correctamente'

    contexto = {
        'formulario':formulario, 'msg':msg
    }
    return render(request,'adminapp/subir.html',contexto)



