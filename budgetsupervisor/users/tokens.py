import datetime

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from users.models import User


class UserTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user: User, timestamp: datetime.time) -> str:
        return f"{user.pk}{timestamp}{user.is_active}"


user_tokenizer = UserTokenGenerator()
