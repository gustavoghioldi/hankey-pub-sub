from django.core.mail import send_mail
from PubSub.settings import EMAIL_HOST_USER
from publisher.pubmodels.message_model import MessageModel

class EmailService:
    @staticmethod
    def send(instance:MessageModel, to, fail_silently=False):
        subject = instance.servicePub.username
        message = str(instance.data)
        send_mail(subject, message, EMAIL_HOST_USER, to, fail_silently=fail_silently)