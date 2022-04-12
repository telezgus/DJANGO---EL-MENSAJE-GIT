from django.db import models
from sqlalchemy import false, null
from sympy import true
from muestra.views import *
from muestra.models import Muestra
from .ordenar import lista

class Obras(models.Model):
    muestra = models.ForeignKey(Muestra,null=True,on_delete=models.CASCADE, default=lista[0])
    apellido = models.CharField(max_length=30,null=True)
    nombre = models.CharField(max_length=30,null=True)
    titulo = models.CharField(max_length=40,null=True)
    fecha = models.CharField(max_length=20,null=True)
    medidas = models.CharField(max_length=20,null=True)
    tecnica = models.CharField(max_length=100,null=True)
    firma = models.TextField(max_length=300,null=True)
    precio =  models.CharField(max_length=20,null=True)
    imagen = models.ImageField(null=True,upload_to="obras")
    creado = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name="Obra"
        verbose_name_plural="Obras"
        
    
    def __str__(self):
        return self.titulo 

# Create your models here.
