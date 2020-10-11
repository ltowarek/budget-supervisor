from django.contrib.messages import get_messages
from django.urls import resolve, reverse
from utils import get_url_path


def test_login_view_get(client):
    url = reverse("login")
    response = client.get(url)
    assert response.status_code == 200


def test_logout_view_get(client):
    url = reverse("logout")
    response = client.get(url)
    assert response.status_code == 200


def test_sign_up_view_get(client):
    url = reverse("signup")
    response = client.get(url)
    assert response.status_code == 200


def test_profile_update_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("profile")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object"] == user_foo.profile


def test_profile_update_view_get_not_logged_in(client):
    url = reverse("profile")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_profile_update_view_post_redirect(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("profile")
    data = {}
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "profile"


def test_profile_update_view_post_message(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("profile")
    data = {}
    response = client.post(url, data=data)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Profile was updated successfully" in messages


def test_profile_connect_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("profile_connect")
    response = client.get(url)
    assert response.status_code == 200


def test_profile_connect_view_get_not_logged_in(client):
    url = reverse("profile_connect")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_profile_connect_view_post_redirect(
    client, user_foo, login_user, mocker, customers_api
):
    login_user(user_foo)
    url = reverse("profile_connect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "profile"


def test_profile_connect_view_post_message(
    client, user_foo, login_user, mocker, customers_api
):
    login_user(user_foo)
    url = reverse("profile_connect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    response = client.post(url)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Profile was connected successfully" in messages


def test_profile_disconnect_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("profile_disconnect")
    response = client.get(url)
    assert response.status_code == 200


def test_profile_disconnect_view_get_not_logged_in(client):
    url = reverse("profile_disconnect")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_profile_disconnect_view_post_redirect(
    client, user_foo, login_user, mocker, customers_api
):
    login_user(user_foo)
    url = reverse("profile_disconnect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "profile"


def test_profile_disconnect_view_post_message(
    client, user_foo, login_user, mocker, customers_api
):
    login_user(user_foo)
    url = reverse("profile_disconnect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    response = client.post(url)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Profile was disconnected successfully" in messages
