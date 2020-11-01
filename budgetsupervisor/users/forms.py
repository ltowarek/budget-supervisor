from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ["username", "email"]

    def save(self) -> User:
        obj = super().save(commit=False)
        obj.is_active = False
        obj.save()
        return obj


class ProfileConnectForm(forms.Form):
    pass


class ProfileDisconnectForm(forms.Form):
    pass
