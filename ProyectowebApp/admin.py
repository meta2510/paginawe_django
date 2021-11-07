from django.contrib import admin
from .models import Usuarios, Bitacora
#from django.conf import settings
#User = settings.AUTH_USER_MODEL
# Register your models here.


class UsuariosAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Usuarios)
admin.site.register(Bitacora)
#dmin.site.register(User)
