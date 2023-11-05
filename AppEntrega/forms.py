from django import forms
from AppEntrega import models

class IngresoPiloto(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    escuderia = forms.CharField()
    
class NuevaCarrera(forms.Form):
    pista = forms.CharField()
    pais = forms.CharField()
    vueltas = forms.IntegerField()

class contactoForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    correo = forms.EmailField()
    comentario = forms.CharField(max_length=200)