from django.shortcuts import render
from .models import Muestra

# Create your views here.
def muestra(request):
    muestras = Muestra.objects.all()
    return render(request, "muestra/muestras.html",{'muestras' : muestras})

