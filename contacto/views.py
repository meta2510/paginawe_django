from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
# Create your views here.


def contacto(request):
    formulario_contacto = FormularioContacto()

    if request.method == "POST":
        formulario_contacto = FormularioContacto(data=request.POST)
        if formulario_contacto.is_valid():
            Nombre = request.POST.get("nombre")
            Email = request.POST.get("email")
            Contenido = request.POST.get("contenido")

            Email = EmailMessage("Mensaje desde App Django")

            return redirect("/contacto/?valido")
    return render(request, "contacto/contacto.html", {'miformulario': formulario_contacto})

