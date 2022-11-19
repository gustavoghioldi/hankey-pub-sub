from django.db import models

class MessageModel(models.Model):
    serviceNamePub = models.CharField(max_length=64) # esto lo vamos a setear desde la credencial que publique
    data = models.JSONField()
    datetimeMutation = models.DateTimeField()
    url = models.URLField()