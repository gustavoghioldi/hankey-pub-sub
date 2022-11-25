from django.db.models.signals import post_save
from publisher.pubmodels.message_model import MessageModel
from core.tasks.message_dispacher_task import message_dispacher

post_save.connect(message_dispacher, sender=MessageModel)
    