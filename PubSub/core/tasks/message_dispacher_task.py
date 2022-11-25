from django.forms.models import model_to_dict
from django_q.tasks import async_task

from publisher.pubmodels.message_model import MessageModel
from subscribers.models import SubscriberModel

    
def message_dispacher(sender,instance: MessageModel,created:bool, **kwargs)->None:
    if created:
        subs = SubscriberModel.objects.filter(serviceNamePub=instance.serviceNamePub)
        for i in subs:
            async_task('requests.post', i.webhook,  json=model_to_dict(instance))