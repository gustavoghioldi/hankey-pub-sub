from django.core.mail import send_mail
from PubSub.settings import EMAIL_HOST_USER
from publisher.pubmodels.message_model import MessageModel


class EmailService:
    def send(instance:MessageModel, from_email, to_email, message, fail_silently=False):
        subject = instance.servicePub.username
        from_email = EMAIL_HOST_USER
        to = [to_email]
        send_mail(subject, message, from_email, to, fail_silently=fail_silently)