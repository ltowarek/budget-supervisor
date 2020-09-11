from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from saltedge.wrapper import SaltEdgeWrapper


class User(AbstractUser):
    pass


class ProfileManager(models.Manager):
    def create_in_saltedge(self, profile, saltedge: SaltEdgeWrapper):
        data = saltedge.create_customer(profile.user.id)
        profile.external_id = data["data"]["id"]
        profile.save()

    def remove_from_saltedge(self, profile, saltedge: SaltEdgeWrapper):
        data = saltedge.remove_customer(profile.external_id)
        profile.external_id = None
        profile.save()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    external_id = models.BigIntegerField(blank=True, null=True)

    objects = ProfileManager()

    def __str__(self):
        return str(self.user)


def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
