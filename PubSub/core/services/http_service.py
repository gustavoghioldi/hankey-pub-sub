from django.forms.models import model_to_dict
from publisher.pubmodels.message_model import MessageModel
from subscribers.models import SubscriberModel
import requests

class JsonService:
    @staticmethod
    def send(instance, url):
        json = model_to_dict(instance)
        r = requests.post(url=url, data=json)
        return r