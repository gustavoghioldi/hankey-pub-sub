from django.forms.models import model_to_dict
from django_q.tasks import async_task

from publisher.pubmodels.message_model import MessageModel
from subscribers.models import SubscriberModel
from core.services.email_service import EmailService
    
def message_dispacher(sender,instance: MessageModel,created:bool, **kwargs)->None:
    if created:
        subs = SubscriberModel.objects.filter(servicePub=instance.servicePub)
        for i in subs:
            if i.webhook:
                #TODO: pasarlo a un servicio
                async_task('requests.post', i.webhook,  json=model_to_dict(instance))
            if i.email:
                #TODO: hacer un acumolador
                async_task('core.services.email_service.EmailService.send', instance, [i.email])