from django.apps import AppConfig


class MyresumeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myresume'

    def ready(self):
        import myresume.signals
