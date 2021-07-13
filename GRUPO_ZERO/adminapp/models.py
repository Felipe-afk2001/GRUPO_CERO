from django.db import models

# Create your models here.

class usuarios(models.Model):
    id_user=models.IntegerField(primary_key=True, verbose_name='id del usuario')
    nickname=models.CharField(max_length=50, verbose_name='nombre de usuario')
    correo=models.CharField(max_length=320, verbose_name='correo del usuario')
    contraseña=models.CharField(max_length=25, verbose_name='contraseña del usuario')
    imagen=models.CharField(max_length=1000, verbose_name='imagen usuario')
    def __str__(self):
        return self.nickname