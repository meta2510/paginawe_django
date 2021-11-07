from django.contrib import admin
from .models import User
#from django.conf import settings
#User = settings.AUTH_USER_MODEL
# Register your models here.

admin.site.register(User)