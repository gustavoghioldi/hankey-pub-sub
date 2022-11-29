from django.db import models
from publisher.models import PublisherModel
# Create your models here.

class SubscriberModel(models.Model):
    serviceNameSub = models.CharField(max_length=64) # esto lo vamos a setear desde la credencial que publique
    webhook    = models.URLField(blank=True, null=True, default=None)
    email      = models.EmailField(blank=True, null=True, default=None)
    servicePub = models.ManyToManyField(PublisherModel)

    def __str__(self):
        return self.serviceNameSub