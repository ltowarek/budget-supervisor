from typing import Any

from users.models import Profile, User


def create_user_profile(
    sender: str, instance: User, created: bool, **kwargs: Any
) -> None:
    if created:
        Profile.objects.create(user=instance)
