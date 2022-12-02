from django.forms.models import model_to_dict
from django_q.tasks import async_task

from publisher.pubmodels.message_model import MessageModel
from subscribers.models import SubscriberModel
from core.services.email_service import EmailService
from core.services.http_service import JsonService

    
def message_dispacher(sender,instance: MessageModel,created:bool, **kwargs)->None:
    if created:
        subs = SubscriberModel.objects.filter(servicePub=instance.servicePub)
        listofemails = [] 
        for i in subs:
            if i.webhook:
                #TODO: pasarlo a un servicio
                async_task('core.services.http_service.JsonService.send')
            if i.email:
                listofemails.append(i.email)
                if len(listofemails) == 10:
                    for mails in listofemails:
                        async_task('core.services.email_service.EmailService.send', instance, [mails])
                    listofemails.clear()
                    