from django.apps import AppConfig
from django.conf import settings
from django.db.models.signals import post_save


class UsersConfig(AppConfig):
    name = "users"

    def ready(self) -> None:
        from users.signals import create_user_profile

        post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
