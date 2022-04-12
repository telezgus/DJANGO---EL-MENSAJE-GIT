from django.apps import AppConfig
from tabnanny import verbose

class ObrasConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'obras'
    verbose_name = 'obras'