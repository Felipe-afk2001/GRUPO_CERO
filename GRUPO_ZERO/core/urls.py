from django.urls import path
from .views import index,obras,autores,login,gchicago,Autor

urlpatterns = [
    path('',index,name="index"),
    path('obras/<id>',obras,name="obras"),
    path('autores',autores,name="autores"),
    path('login',login,name="login"),
    path('gchicago',gchicago,name="gchicago"),
    path('autor/<id>',Autor,name="autor"),
]
