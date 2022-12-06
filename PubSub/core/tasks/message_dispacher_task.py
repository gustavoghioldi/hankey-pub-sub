from django_q.tasks import async_task
from publisher.pubmodels.message_model import MessageModel
from subscribers.models import SubscriberModel
from core.services.email_service import EmailService
from core.services.http_service import JsonService
from PubSub.settings import EMAIL_HOST_USER

dictofemails=[]

def message_dispacher(sender,instance: MessageModel,created:bool, **kwargs)->None:
    if created:
        subs = SubscriberModel.objects.filter(servicePub=instance.servicePub)
        for i in subs:
            if i.webhook:
                #TODO: pasarlo a un servicio
                async_task('core.services.http_service.JsonService.send', instance, i.webhook)
            if i.email:
                dictofemails.append({(i.email) : str(instance.data)})
                if len(dictofemails) >= 2:
                    for members in dictofemails:
                        for clave, valor in members.items():
                            async_task('core.services.email_service.EmailService.send',instance, EMAIL_HOST_USER, clave, valor)
                    dictofemails.clear()
                    break
                else:
                    break        

                