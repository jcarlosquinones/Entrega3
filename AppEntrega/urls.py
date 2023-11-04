from django.urls import path
from AppEntrega.views import *

urlpatterns = [
    path('', inicio,name= "home"),
    path('pilotos/', pilotos),
    path('carreras/', carreras),
    path('contacto/', contacto),
    path('ingreso/', ingreso),
]