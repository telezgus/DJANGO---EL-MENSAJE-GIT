from django.apps import AppConfig
from tabnanny import verbose

class SubastaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'subasta'
    verbose_name = 'subasta'