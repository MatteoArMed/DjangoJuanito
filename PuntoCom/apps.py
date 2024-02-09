from django.apps import AppConfig


class PuntocomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PuntoCom'

    def ready(self):
        import PuntoCom.signals
