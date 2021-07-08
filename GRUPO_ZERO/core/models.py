from django.db import models

# Create your models here.
class categorias(models.Model):
    id_categoria=models.IntegerField(primary_key=True, verbose_name='id de la categoria')
    nombrec=models.CharField(max_length=25, verbose_name='nombre de la categoria')
    imagen=models.ImageField(verbose_name='imagen de la categoria')
    def __str__(self):
        return self.nombrec

class autor(models.Model):
    id_autor=models.IntegerField(primary_key=True, verbose_name='id del autor')
    nombrea=models.CharField(max_length=50, verbose_name='nombre del autor')
    descripcion=models.CharField(max_length=250, verbose_name='descripcion del autor')
    imagen=models.ImageField(verbose_name='imagen autor')
    categorias=models.ForeignKey(categorias,on_delete=models.CASCADE)
    def __str__(self):
        return self.nombrea

class obras(models.Model):
    id_obra=models.IntegerField(primary_key=True,verbose_name='id de la obra')
    nombreo=models.CharField(max_length=30, verbose_name='nombre de la obra')
    descripcion=models.CharField(max_length=250, verbose_name='descripcion de la obra')
    imagen=models.ImageField(verbose_name='imagen de la obra')
    precio=models.IntegerField(verbose_name='precio de la obra')
    autor=models.ForeignKey(autor, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreo

class usuarios(models.Model):
    id_user=models.IntegerField(primary_key=True, verbose_name='id del usuario')
    nickname=models.CharField(max_length=30, verbose_name='nombre de usuario')
    correo=models.CharField(max_length=320, verbose_name='correo del usuario')
    contraseña=models.CharField(max_length=25, verbose_name='contraseña del usuario')
    imagen=models.ImageField(verbose_name='imagen del usuario')
    def __str__(self):
        return self.nickname