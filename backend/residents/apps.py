from django.apps import AppConfig

default_app_config = "residents.apps.ResidentsConfig"


class ResidentsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "residents"

    def ready(self):
        import residents.signals
