from django.db import models
from django.contrib.auth.models import AbstractUser

class PublisherModel(AbstractUser):
    is_service = models.BooleanField(default=False)