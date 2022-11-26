from django.db import models
from publisher.pubmodels.message_model import MessageModel
 
# Create your models here.

class SubscriberModel(models.Model):
    serviceNameSub = models.CharField(max_length=64) # esto lo vamos a setear desde la credencial que publique
    webhook = models.URLField()
    #TODO: CAMBIAR A EVENTOS
    serviceNamePub = models.ForeignKey(MessageModel, on_delete= models.CASCADE, to_field="serviceNamePub")

    def __str__(self):
        return self.serviceNameSub