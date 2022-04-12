from django.apps import AppConfig
from tabnanny import verbose

class MuestraConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'muestra'
    verbose_name = 'Muestra'