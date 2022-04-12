from django.db import models
from sqlalchemy import false, null
from sympy import true



class Subasta(models.Model):
    lote = models.IntegerField(null=True)
    apellido = models.CharField(max_length=30,null=True)
    nombre = models.CharField(max_length=30,null=True)
    titulo = models.CharField(max_length=40,null=True)
    medidas = models.CharField(max_length=20,null=True)
    tecnica = models.CharField(max_length=100,null=True)
    firma = models.TextField(max_length=300,null=True)
    base =  models.CharField(max_length=20,null=True)
    imagen = models.ImageField(null=True,upload_to="subasta")
    creado = models.DateTimeField(auto_now_add = True)
    class Meta:
        verbose_name="Subasta"
        verbose_name_plural="Subastas"
        
    
    def __str__(self):
        return self.titulo 