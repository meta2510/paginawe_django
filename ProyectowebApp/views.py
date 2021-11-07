from django.shortcuts import render, HttpResponse

from servicios.models import servicio
from blog.models import Post, Categoria

# Crear las vistas


def home(request):

    return render(request, "ProyectowebApp/home.html")
