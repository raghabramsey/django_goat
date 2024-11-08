from django.apps import AppConfig

class GoatsConfig(AppConfig):
    name = 'goats'

    def ready(self):
        import goats.signals
