from django.shortcuts import render
from .models import Subasta


def subasta(request):
    subastas = Subasta.objects.all()
    return render(request, "subasta/catalogo.html",{'subastas' : subastas})
