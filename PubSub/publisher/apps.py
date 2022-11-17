from django.apps import AppConfig


class PublisherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "publisher"

    def ready(self) -> None:
        #from publisher.models.publisher_model import PublisherModel
        return super().ready()