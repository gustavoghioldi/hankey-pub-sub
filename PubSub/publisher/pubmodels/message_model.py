from django.db import models
from publisher.models import PublisherModel

class MessageModel(models.Model):
    servicePub = models.ForeignKey(PublisherModel, on_delete= models.CASCADE)
    data = models.JSONField()
    datetimeMutation = models.DateTimeField()
    url = models.URLField()

    def __str__(self):
        return str(self.id)
    
    