from users.forms import (
    SignUpForm,
    ProfileConnectForm,
    ProfileDisconnectForm,
)
import pytest


@pytest.mark.django_db
def test_sign_up_form_valid():
    data = {"username": "xyz", "password1": "Django 3", "password2": "Django 3"}
    form = SignUpForm(data=data)
    assert form.is_valid() is True


def test_profile_connect_form_valid():
    data = {}
    form = ProfileConnectForm(data=data)
    assert form.is_valid() is True


def test_profile_disconnect_form_valid():
    data = {}
    form = ProfileDisconnectForm(data=data)
    assert form.is_valid() is True
