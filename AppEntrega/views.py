from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega.models import *
from AppEntrega.forms import *

# Create your views here.

def inicio(request):
    return render(request, "AppEntrega/index.html")

def pilotos(request):
    return render(request, "AppEntrega/pilotos.html")

def carreras(request):
    return render(request, "AppEntrega/carreras.html")

def contacto(request):
    return render(request, "AppEntrega/contacto.html")

def ingreso(request):
    return render(request, "AppEntrega/ingreso.html")

#Vistas de los formularios

def pilotoForm(request):
    if request.method == 'POST':
        mi_Formulario = IngresoPiloto(request.POST)
        print(mi_Formulario)
        if mi_Formulario.is_valid():
            informacion = mi_Formulario.cleaned_data
            nuevopiloto = (informacion['nombre'], informacion['apellido'], informacion['escuderia'])
            nuevopiloto.save()
            return render(request, "AppEntrega/index.html")
    else:
        mi_Formulario = IngresoPiloto()  
        return render(request, "AppEntrega/pilotos.html", {"mi_Formulario":mi_Formulario})