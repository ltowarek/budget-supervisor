from django import forms
from django.contrib.auth.forms import UserCreationForm
from saltedge.saltedge import SaltEdge
from .models import Profile, User
import os
import json


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username"]


class ProfileConnectForm(forms.Form):
    pass
