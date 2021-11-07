from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from mirage import fields
import datetime


# Create your models here.
class UserManager(BaseUserManager, models.Manager):
    #        use_in_migrations = True

    def _create_user(self, username,email, password,is_staff,is_superuser,**extra_fields):
        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email es obligatorio')
        user = self.model(username = username, email = email,is_active=True, is_staff=is_staff,
        is_superuser = is_superuser, **extra_fields)
        
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password= None , **extra_fields):
        return self._create_user(username, email, password, False, False, **extra_fields)
    
    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username,email,password, True, True,**extra_fields)



class User(AbstractBaseUser, PermissionsMixin):
    PRIVILEGIOS = (
        ('A', 'Administrador'),
        ('V', 'Usuario vendedor'),
        ('R', 'Usuario reporte'),
        ('U', 'Usuario'),
    )

    TIENDAS = (
        ('M', 'Miraflores'),
        ('T', 'Tikal Futura'),
        ('E', 'Eskala Roosevelt'),
        ('NA', 'NA'),
    )

    username = models.CharField(unique=True, max_length=50)
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    edad = models.PositiveIntegerField(null=True)
    imagen = models.ImageField(upload_to='Usuario',null=True, blank=True)
    privilegio = models.CharField(max_length=1, choices=PRIVILEGIOS)
    created = models.DateTimeField(default=datetime.datetime.now())
    updated = models.DateTimeField(default=datetime.datetime.now())
    tienda = models.CharField(max_length=2, choices=TIENDAS)


    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default = False)
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_short_name(self):
        return self.first_name