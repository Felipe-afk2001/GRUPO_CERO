from django.urls import path
from .views import subir

urlpatterns = [
   path('',subir,name="subir"),
]