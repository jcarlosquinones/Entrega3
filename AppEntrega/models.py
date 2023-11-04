from django.db import models

# Create your models here.

class Piloto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    escuderia = models.CharField(max_length=40)
    
class Carreras(models.Model):
    pista = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    vueltas = models.IntegerField()
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)    
    correo = models.EmailField()
    comentario = models.CharField(max_length=200)
    
