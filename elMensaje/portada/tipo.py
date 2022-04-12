from muestra.models import Muestra
from obras.models import Obras

obras = Obras.objects.all()
muestras = Muestra.objects.all()
for muestra in muestras:
    ultima= muestra.id
