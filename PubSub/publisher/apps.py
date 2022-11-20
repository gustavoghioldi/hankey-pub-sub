from django.apps import AppConfig


class PublisherConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "publisher"

    def ready(self) -> None:
        from publisher.signals import publish_model_post_save
        from publisher.pubmodels.message_model import MessageModel
        from publisher.pubmodels.publish_model import PublisherModel
        return super().ready()