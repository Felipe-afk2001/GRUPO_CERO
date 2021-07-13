from django.urls import path
from .views import eliminar, subir , modificar,   mostrar

urlpatterns = [
   path('',mostrar,name="mostrar"),
   path('subir/',subir,name="subir"),
   path('modificar/<id>',modificar,name="modificar"),
   path('eliminar/<id>',eliminar,name="eliminar"),
]