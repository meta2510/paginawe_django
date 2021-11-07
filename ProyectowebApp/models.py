from django.db import models
from mirage import fields

# Create your models here.


class Usuarios(models.Model):
    PRIVILEGIOS = (
        ('A', 'Administrador'),
        ('V', 'Usuario vendedor'),
        ('R', 'Usuario reporte'),
    )
    username = models.CharField(max_length=50, primary_key=True)
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    imagen = models.ImageField(upload_to='Usuario')
    password = fields.EncryptedCharField()
    privilegio = models.CharField(max_length=1, choices=PRIVILEGIOS)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)


class Bitacora(models.Model):
    fecha = models.DateTimeField(auto_now=True, blank=True)
    username = models.CharField(max_length=50)
    ip_addres = models.GenericIPAddressField()
    accion = models.TextField()
