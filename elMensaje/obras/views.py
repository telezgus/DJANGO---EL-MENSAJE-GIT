from django.shortcuts import render
from sympy import O
from .models import Obras
from muestra.models import Muestra

# Create your views here.
def obras(request):    
    obras = Obras.objects.all()
    muestra_id = request.GET.get("lang")
    artista = Muestra.objects.filter(id = muestra_id)     
    obras = obras.filter(muestra = muestra_id) 
    return render(request, "obras/obras.html",{'obras' : obras,'artista' : artista})

