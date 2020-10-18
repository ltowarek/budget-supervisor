from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    external_id = models.BigIntegerField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.user)
