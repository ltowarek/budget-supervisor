from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username"]


class ProfileConnectForm(forms.Form):
    pass
