from tabnanny import verbose
from django.db import models
from sqlalchemy import false, null
from sympy import true
from .opcion import opciones
from .tipo import ultima


class Portada(models.Model):
    evento = models.CharField(max_length=20,null=True)
    opcion = models.CharField(max_length=30, choices= opciones)
    muestra = ultima
    artista = models.CharField(max_length=30)
    titulo = models.CharField(max_length=50,null=false)
    fecha = models.CharField(max_length=20)
    obra1 = models.ImageField(null=false,upload_to="portada")
    obra2 = models.ImageField(null=false,upload_to="portada")
    creado = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name="Portada"
        verbose_name_plural="Portadas"
        
    
    def __str__(self):
        return self.evento 
    
    
# Create your models here.
