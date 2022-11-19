from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.cache import cache
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms.models import model_to_dict

class PublisherModel(AbstractUser):
    is_service = models.BooleanField(default=False)
    
def publisher_model_post_save(sender,instance: PublisherModel,**kwargs):
    cache.set(instance.last_name,instance.first_name)
    

post_save.connect(publisher_model_post_save, sender=PublisherModel)
