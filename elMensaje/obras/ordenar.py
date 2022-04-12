from muestra.models import Muestra

   

    

lista = list(reversed(Muestra.objects.all().values_list("id", "artista")))