from django.db import models
from django.conf import settings
from phone_field import PhoneField

# Create your models here.

class Address(models.Model):
    METODO_PAGO = (
    ('Efectivo', 'Efectivo'),
    ('POS MOVIL', 'POS MOVIL')
)

    TIENDAS = (
        ('Miraflores', 'Miraflores'),
        ('Tikal Futura', 'Tikal Futura'),
        ('Eskala Roosevelt', 'Eskala Roosevelt'),
    )

    #numero_orden = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(max_length=100)
    #username = models.ForeignKey(settings.AUTH_USER_MODEL,
     #                        on_delete=models.CASCADE,null=True)
    direccion = models.CharField(max_length=100)
    municipio = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    metodo_pago = models.CharField(choices=METODO_PAGO, max_length=9)
    tienda = models.CharField(choices=TIENDAS, max_length=16)
    #def __str__(self):
     #   return self.user.username



class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, blank=True, null=True)
    numero_orden = models.AutoField(primary_key=True)
    productos = models.TextField(blank=True)
    cantidad = models.IntegerField() #amount
    total = models.FloatField() #
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username