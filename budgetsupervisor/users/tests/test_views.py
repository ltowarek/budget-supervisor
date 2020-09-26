from django.urls import reverse


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


def test_profile_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("profile")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object"] == user_foo.profile


def test_profile_view_get_not_logged_in(client):
    url = reverse("profile")
    response = client.get(url)
    assert response.status_code == 302


def test_profile_connect_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("profile_connect")
    response = client.get(url)
    assert response.status_code == 200


def test_profile_connect_view_get_not_logged_in(client):
    url = reverse("profile_connect")
    response = client.get(url)
    assert response.status_code == 302


def test_profile_connect_view_post(client, user_foo, login_user, mocker, customers_api):
    login_user(user_foo)
    url = reverse("profile_connect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    response = client.post(url, follow=True)
    assert response.status_code == 200
