from tabnanny import verbose
from django.apps import AppConfig


class PortadaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'portada'
    verbose_name = 'Portada'
