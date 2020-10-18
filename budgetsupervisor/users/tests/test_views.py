from typing import Callable, Dict

import swagger_client as saltedge_client
from budget.models import Account, Connection, Transaction
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import resolve, reverse
from pytest_mock import MockFixture
from users.models import User
from utils import get_url_path


def test_login_view_get(client: Client) -> None:
    url = reverse("login")
    response = client.get(url)
    assert response.status_code == 200


def test_logout_view_get(client: Client) -> None:
    url = reverse("logout")
    response = client.get(url)
    assert response.status_code == 200


def test_sign_up_view_get(client: Client) -> None:
    url = reverse("signup")
    response = client.get(url)
    assert response.status_code == 200


def test_profile_update_view_get(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("profile")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["object"] == user_foo.profile


def test_profile_update_view_get_not_logged_in(client: Client) -> None:
    url = reverse("profile")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_profile_update_view_post_redirect(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("profile")
    data: Dict = {}
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "profile"


def test_profile_update_view_post_message(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("profile")
    data: Dict = {}
    response = client.post(url, data=data)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Profile was updated successfully" in messages


def test_profile_connect_view_get(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("profile_connect")
    response = client.get(url)
    assert response.status_code == 200


def test_profile_connect_view_get_not_logged_in(client: Client) -> None:
    url = reverse("profile_connect")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_profile_connect_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    mocker: MockFixture,
    customers_api: saltedge_client.CustomersApi,
) -> None:
    login_user(user_foo)
    url = reverse("profile_connect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "profile"


def test_profile_connect_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    mocker: MockFixture,
    customers_api: saltedge_client.CustomersApi,
) -> None:
    login_user(user_foo)
    url = reverse("profile_connect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    response = client.post(url)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Profile was connected successfully" in messages


def test_profile_disconnect_view_get(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("profile_disconnect")
    response = client.get(url)
    assert response.status_code == 200


def test_profile_disconnect_view_get_not_logged_in(client: Client) -> None:
    url = reverse("profile_disconnect")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_profile_disconnect_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    mocker: MockFixture,
    customers_api: saltedge_client.CustomersApi,
) -> None:
    login_user(user_foo)
    url = reverse("profile_disconnect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "profile"


def test_profile_disconnect_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    mocker: MockFixture,
    customers_api: saltedge_client.CustomersApi,
) -> None:
    login_user(user_foo)
    url = reverse("profile_disconnect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    response = client.post(url)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Profile was disconnected successfully" in messages


def test_profile_disconnect_view_post_delete_connections(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
    mocker: MockFixture,
    customers_api: saltedge_client.CustomersApi,
) -> None:
    login_user(user_foo)
    url = reverse("profile_disconnect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    response = client.post(url)
    assert response.status_code == 302
    assert not Connection.objects.filter(pk=connection_foo.pk).exists()


def test_profile_disconnect_view_post_disconnect_accounts(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo_external: Account,
    mocker: MockFixture,
    customers_api: saltedge_client.CustomersApi,
    connections_api: saltedge_client.ConnectionsApi,
) -> None:
    login_user(user_foo)
    url = reverse("profile_disconnect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    mocker.patch(
        "budget.views.connections_api", autospec=True, return_value=connections_api
    )
    response = client.post(url)
    assert response.status_code == 302
    account_foo_external.refresh_from_db()
    assert account_foo_external.external_id is None


def test_profile_disconnect_view_post_disconnect_transactions(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    transaction_foo_external: Transaction,
    mocker: MockFixture,
    customers_api: saltedge_client.CustomersApi,
    connections_api: saltedge_client.ConnectionsApi,
) -> None:
    login_user(user_foo)
    url = reverse("profile_disconnect")
    mocker.patch("users.views.customers_api", autospec=True, return_value=customers_api)
    mocker.patch(
        "budget.views.connections_api", autospec=True, return_value=connections_api
    )
    response = client.post(url)
    assert response.status_code == 302
    transaction_foo_external.refresh_from_db()
    assert transaction_foo_external.external_id is None


def test_user_delete_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    customers_api: saltedge_client.CustomersApi,
) -> None:
    login_user(user_foo)
    url = reverse("user_delete")
    response = client.get(url)
    assert response.status_code == 200


def test_user_delete_view_get_not_logged_in(client: Client) -> None:
    url = reverse("user_delete")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_user_delete_view_post_redirect(
    client: Client, user_foo: User, login_user: Callable[[User], None],
) -> None:
    login_user(user_foo)
    url = reverse("user_delete")
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_user_delete_view_post_message(
    client: Client, user_foo: User, login_user: Callable[[User], None],
) -> None:
    login_user(user_foo)
    url = reverse("user_delete")
    response = client.post(url)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "User was deleted successfully" in messages
