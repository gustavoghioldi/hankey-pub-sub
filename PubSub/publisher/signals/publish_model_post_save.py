from django.core.cache import cache
from django.db.models.signals import post_save
from publisher.models import PublisherModel

def publisher_model_post_save(sender,instance: PublisherModel,**kwargs):
    cache.set(instance.last_name,instance.first_name)
    

post_save.connect(publisher_model_post_save, sender=PublisherModel)