from django import forms

class IngresoPiloto(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    escuderia = forms.CharField()