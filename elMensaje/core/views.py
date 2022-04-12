from django.shortcuts import render, HttpResponse


# Create your views here.
def contacto(request):
    return render(request, "core/contacto.html")

def compra(request):
    return render(request, "core/compra.html")

def terms(request):
    return render(request, "core/terms.html")