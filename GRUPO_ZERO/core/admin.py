from django.contrib import admin
from .models import autor, obras, categorias, usuarios
# Register your models here.

admin.site.register(autor)
admin.site.register(obras)
admin.site.register(categorias)
admin.site.register(usuarios)