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
            nuevopiloto = mi_Formulario.cleaned_data
            nuevopiloto = Piloto(nombre=nuevopiloto['nombre'], apellido=nuevopiloto['apellido'], escuderia=nuevopiloto['escuderia'])
            nuevopiloto.save()
            return render(request, "AppEntrega/index.html")
    else:
        mi_Formulario = IngresoPiloto()  
        return render(request, "AppEntrega/pilotos.html", {"mi_Formulario":mi_Formulario})

def carreraForm(request):
    if request.method == 'POST':
        mi_Formulario = NuevaCarrera(request.POST)
        print(mi_Formulario)
        if mi_Formulario.is_valid():
            nuevapista = mi_Formulario.cleaned_data
            nuevapista = Carreras(pista=nuevapista['pista'], pais=nuevapista['pais'], vueltas=nuevapista['vueltas'])
            nuevapista.save()
            return render(request, "AppEntrega/index.html")
    else:
        mi_Formulario = NuevaCarrera()
        return render(request, "AppEntrega/carreras.html", {"mi_Formulario":mi_Formulario})