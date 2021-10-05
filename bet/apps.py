from django.apps import AppConfig


class BetConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bet'

    def ready(self):
        from bet.jobs import updater
        updater.start()