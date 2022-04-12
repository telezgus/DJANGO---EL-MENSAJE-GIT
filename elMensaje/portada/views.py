from django.shortcuts import render
from .models import Portada

# Create your views here.
def index(request):
    portada = Portada.objects.all()
    return render(request, "portada/index.html",{'portada' : portada})