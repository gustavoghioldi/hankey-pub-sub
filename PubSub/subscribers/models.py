from django.db import models

# Create your models here.
class SubscriberModel(models.Model):
    serviceNameSub = models.CharField(max_length=64) # esto lo vamos a setear desde la credencial que publique
    webhook = models.URLField()
    #TODO: CAMBIAR A EVENTOS
    serviceNamePub = models.CharField(max_length=64)