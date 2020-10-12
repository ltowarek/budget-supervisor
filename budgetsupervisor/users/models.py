from typing import Any

import swagger_client as saltedge_client
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save


class User(AbstractUser):
    pass


class ProfileManager(models.Manager):
    def create_in_saltedge(
        self, profile: Any, api: saltedge_client.CustomersApi
    ) -> None:
        data = saltedge_client.CustomerRequestBodyData(
            identifier=str(profile.user.username)
        )
        body = saltedge_client.CustomerRequestBody(data)
        response = api.customers_post(body=body)
        profile.external_id = int(response.data.id)
        profile.save()

    def remove_from_saltedge(
        self, profile: Any, api: saltedge_client.CustomersApi
    ) -> None:
        api.customers_customer_id_delete(str(profile.external_id))
        profile.external_id = None
        profile.save()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    external_id = models.BigIntegerField(blank=True, null=True)

    objects = ProfileManager()

    def __str__(self) -> str:
        return str(self.user)


def create_user_profile(
    sender: str, instance: User, created: bool, **kwargs: int
) -> None:
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
