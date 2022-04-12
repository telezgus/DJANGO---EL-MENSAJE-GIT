from unicodedata import name
from django.db import models
from sqlalchemy import false, null
from sympy import true


class Muestra(models.Model):
    artista = models.CharField(max_length=30)
    fecha = models.CharField(max_length=30,null=True,blank=True)
    titulo = models.CharField(max_length=30,null=True,blank=True)
    descripcion = models.TextField(max_length=300,null=True,blank=True)
    creado = models.DateTimeField(auto_now_add = True,blank=True)
    class Meta:
        verbose_name="Muestra"
        verbose_name_plural="Muestras"
        
    
    def __str__(self):
        return "{},{}".format(self.artista, self.id) 

# Create your models here.
