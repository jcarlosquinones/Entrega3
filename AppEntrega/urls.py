from django.urls import path
from AppEntrega.views import *

urlpatterns = [
    path('', inicio,name= "home"),
    path('pilotos/', pilotos),
    path('carreras/', carreras),
    path('contacto/', contactForm),
    path('ingreso/', ingreso),
    path('nuevopiloto/', pilotoForm),
    path('nuevacarrera/', carreraForm),
    path('opcionespiloto/', opcionespiloto),
]