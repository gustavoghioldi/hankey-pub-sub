from django.db import models
from django.contrib.auth.models import AbstractUser


class PublisherModel(AbstractUser):
    is_service = models.BooleanField(default=False)

    def clean(self):
        super().clean()
        self.set_password(self.password) ## convertir a sha256 el password