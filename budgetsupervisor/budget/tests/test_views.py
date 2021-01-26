import base64
import datetime
import json
from typing import Callable, Dict

import OpenSSL.crypto
import pytest
import swagger_client as saltedge_client
import swagger_client.rest
from budget.models import Account, Category, Connection, Transaction
from budget.views import verify_signature
from django.contrib.messages import get_messages
from django.test import Client
from django.urls import resolve, reverse
from pytest_mock import MockFixture
from swagger_client import ConnectSessionResponse, ConnectSessionResponseData
from users.models import Profile, User
from utils import get_url_path


def test_index_view_get(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("budget_index")
    response = client.get(url)
    assert response.status_code == 200


def test_index_view_get_not_logged_in(client: Client) -> None:
    url = reverse("budget_index")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_list_view_get_single_connection(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["connection_list"]) == [connection_foo]


def test_connection_list_view_get_not_logged_in(client: Client) -> None:
    url = reverse("connections:connection_list")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_list_view_get_multiple_connections(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_factory: Callable[..., Connection],
) -> None:
    login_user(user_foo)
    connection_a = connection_factory("a")
    connection_b = connection_factory("b")
    url = reverse("connections:connection_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["connection_list"]) == [connection_a, connection_b]


def test_connection_list_view_get_ordered_by_provider(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_factory: Callable[..., Connection],
) -> None:
    login_user(user_foo)
    connection_b = connection_factory("b")
    connection_a = connection_factory("a")
    url = reverse("connections:connection_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["connection_list"]) == [connection_a, connection_b]


def test_connection_list_view_get_current_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    connection_factory: Callable[..., Connection],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    connection_a = connection_factory("a", user=user_a)
    connection_factory("b", user=user_b)
    url = reverse("connections:connection_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["connection_list"]) == [connection_a]


def test_connection_create_view_get(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_create")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["profile"] == user_foo.profile


def test_connection_create_view_get_not_logged_in(client: Client) -> None:
    url = reverse("connections:connection_create")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_create_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    mocker: MockFixture,
    connect_sessions_api: saltedge_client.ConnectSessionsApi,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_create")
    connect_sessions_api.connect_sessions_create_post.return_value = ConnectSessionResponse(
        data=ConnectSessionResponseData(connect_url="example.com")
    )
    mocker.patch(
        "budget.views.connect_sessions_api",
        autospec=True,
        return_value=connect_sessions_api,
    )
    response = client.post(url)
    assert response.status_code == 302
    assert response.url == "example.com"


def test_connection_update_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_update", kwargs={"pk": connection_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_connection_update_view_get_not_logged_in(
    client: Client, connection_foo: Connection
) -> None:
    url = reverse("connections:connection_update", kwargs={"pk": connection_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_update_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_update", kwargs={"pk": connection_foo.pk})
    response = client.post(url, data={})
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "connection_list"


def test_connection_update_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_update", kwargs={"pk": connection_foo.pk})
    data = {
        "provider": "bar",
    }
    response = client.post(url, data=data)
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Connection was updated successfully" in messages


def test_connection_update_view_post_different_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    connection_factory: Callable[..., Connection],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    connection_factory("a", user=user_a)
    connection_b = connection_factory("b", user=user_b)
    url = reverse("connections:connection_update", kwargs={"pk": connection_b.pk})
    data = {"name": "bx", "connection_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 403


def test_connection_refresh_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_refresh", kwargs={"pk": connection_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_connection_refresh_view_get_not_logged_in(
    client: Client, connection_foo: Connection
) -> None:
    url = reverse("connections:connection_refresh", kwargs={"pk": connection_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_refresh_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
    mocker: MockFixture,
    connect_sessions_api: saltedge_client.ConnectSessionsApi,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_refresh", kwargs={"pk": connection_foo.pk})
    connect_sessions_api.connect_sessions_refresh_post.return_value = ConnectSessionResponse(
        data=ConnectSessionResponseData(connect_url="example.com")
    )
    mocker.patch(
        "budget.views.connect_sessions_api",
        autospec=True,
        return_value=connect_sessions_api,
    )
    response = client.post(url, data={})
    assert response.status_code == 302
    assert response.url == "example.com"


def test_connection_refresh_view_post_different_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    connection_factory: Callable[..., Connection],
    mocker: MockFixture,
    connect_sessions_api: saltedge_client.ConnectSessionsApi,
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    connection_factory("a", user=user_a)
    connection_b = connection_factory("b", user=user_b)
    url = reverse("connections:connection_refresh", kwargs={"pk": connection_b.pk})
    data: Dict = {}
    connect_sessions_api.connect_sessions_refresh_post.return_value = ConnectSessionResponse(
        data=ConnectSessionResponseData(connect_url="example.com")
    )
    mocker.patch(
        "budget.views.connect_sessions_api",
        autospec=True,
        return_value=connect_sessions_api,
    )
    response = client.post(url, data=data)
    assert response.status_code == 403


def test_connection_delete_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_delete", kwargs={"pk": connection_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_connection_delete_view_get_not_logged_in(
    client: Client, connection_foo: Connection
) -> None:
    url = reverse("connections:connection_delete", kwargs={"pk": connection_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_delete_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
    mocker: MockFixture,
    connections_api: saltedge_client.ConnectionsApi,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_delete", kwargs={"pk": connection_foo.pk})
    mocker.patch(
        "budget.views.connections_api", autospec=True, return_value=connections_api
    )
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "connection_list"


def test_connection_delete_view_post_disconnect_accounts(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
    account_foo_external: Account,
    mocker: MockFixture,
    connections_api: saltedge_client.ConnectionsApi,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_delete", kwargs={"pk": connection_foo.pk})
    mocker.patch(
        "budget.views.connections_api", autospec=True, return_value=connections_api
    )
    response = client.post(url)
    assert response.status_code == 302
    account_foo_external.refresh_from_db()
    assert account_foo_external.external_id is None


def test_connection_delete_view_post_disconnect_transactions(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
    transaction_foo_external: Transaction,
    mocker: MockFixture,
    connections_api: saltedge_client.ConnectionsApi,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_delete", kwargs={"pk": connection_foo.pk})
    mocker.patch(
        "budget.views.connections_api", autospec=True, return_value=connections_api
    )
    response = client.post(url)
    assert response.status_code == 302
    transaction_foo_external.refresh_from_db()
    assert transaction_foo_external.external_id is None


def test_connection_delete_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    connection_foo: Connection,
    mocker: MockFixture,
    connections_api: saltedge_client.ConnectionsApi,
) -> None:
    login_user(user_foo)
    url = reverse("connections:connection_delete", kwargs={"pk": connection_foo.pk})
    mocker.patch(
        "budget.views.connections_api", autospec=True, return_value=connections_api
    )
    response = client.post(url)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Connection was deleted successfully" in messages


def test_connection_delete_view_post_different_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    connection_factory: Callable[..., Connection],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    connection_factory("a", user=user_a)
    connection_b = connection_factory("b", user=user_b)
    url = reverse("connections:connection_delete", kwargs={"pk": connection_b.pk})
    response = client.post(url)
    assert response.status_code == 403


def test_account_list_view_get_single_account(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo: Account,
) -> None:
    login_user(user_foo)
    url = reverse("accounts:account_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["account_list"]) == [account_foo]


def test_account_list_view_get_not_logged_in(client: Client) -> None:
    url = reverse("accounts:account_list")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_account_list_view_get_multiple_accounts(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_factory: Callable[..., Account],
) -> None:
    login_user(user_foo)
    account_a = account_factory("a")
    account_b = account_factory("b")
    url = reverse("accounts:account_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["account_list"]) == [account_a, account_b]


def test_account_list_view_get_ordered_by_name(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_factory: Callable[..., Account],
) -> None:
    login_user(user_foo)
    account_b = account_factory("b")
    account_a = account_factory("a")
    url = reverse("accounts:account_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["account_list"]) == [account_a, account_b]


def test_account_list_view_get_current_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    account_factory: Callable[..., Account],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    account_a = account_factory("a", user=user_a)
    account_factory("b", user=user_b)
    url = reverse("accounts:account_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["account_list"]) == [account_a]


def test_account_create_view_get(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("accounts:account_create")
    response = client.get(url)
    assert response.status_code == 200


def test_account_create_view_get_not_logged_in(client: Client) -> None:
    url = reverse("accounts:account_create")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_account_create_view_post_redirect(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("accounts:account_create")
    data = {"name": "a", "account_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "account_list"


def test_account_create_view_post_message(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("accounts:account_create")
    data = {"name": "a", "account_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Account was created successfully" in messages


def test_account_update_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo: Account,
) -> None:
    login_user(user_foo)
    url = reverse("accounts:account_update", kwargs={"pk": account_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_account_update_view_get_not_logged_in(
    client: Client, account_foo: Account
) -> None:
    url = reverse("accounts:account_update", kwargs={"pk": account_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_account_update_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo: Account,
) -> None:
    login_user(user_foo)
    url = reverse("accounts:account_update", kwargs={"pk": account_foo.pk})
    data = {"name": "bar", "account_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "account_list"


def test_account_update_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo: Account,
) -> None:
    login_user(user_foo)
    url = reverse("accounts:account_update", kwargs={"pk": account_foo.pk})
    data = {"name": "bar", "account_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Account was updated successfully" in messages


def test_account_update_view_post_different_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    account_factory: Callable[..., Account],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    account_factory("a", user=user_a)
    account_b = account_factory("b", user=user_b)
    url = reverse("accounts:account_update", kwargs={"pk": account_b.pk})
    data = {"name": "bx", "account_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 403


def test_account_delete_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo: Account,
) -> None:
    login_user(user_foo)
    url = reverse("accounts:account_delete", kwargs={"pk": account_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_account_delete_view_get_not_logged_in(
    client: Client, account_foo: Account
) -> None:
    url = reverse("accounts:account_delete", kwargs={"pk": account_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_account_delete_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo: Account,
) -> None:
    login_user(user_foo)
    url = reverse("accounts:account_delete", kwargs={"pk": account_foo.pk})
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "account_list"


def test_account_delete_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo: Account,
) -> None:
    login_user(user_foo)
    url = reverse("accounts:account_delete", kwargs={"pk": account_foo.pk})
    response = client.post(url)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Account was deleted successfully" in messages


def test_account_delete_view_post_different_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    account_factory: Callable[..., Account],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    account_factory("a", user=user_a)
    account_b = account_factory("b", user=user_b)
    url = reverse("accounts:account_delete", kwargs={"pk": account_b.pk})
    response = client.post(url)
    assert response.status_code == 403


def test_transaction_list_view_get_single_transaction(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    transaction_foo: Transaction,
) -> None:
    login_user(user_foo)
    url = reverse("transactions:transaction_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["transaction_list"]) == [transaction_foo]


def test_transaction_list_view_get_not_logged_in(client: Client) -> None:
    url = reverse("transactions:transaction_list")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_transaction_list_view_get_multiple_transactions(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    transaction_factory: Callable[..., Transaction],
) -> None:
    login_user(user_foo)
    transaction_a = transaction_factory()
    transaction_b = transaction_factory()
    url = reverse("transactions:transaction_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["transaction_list"]) == [transaction_a, transaction_b]


def test_transaction_list_view_get_ordered_by_date(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    transaction_factory: Callable[..., Transaction],
) -> None:
    login_user(user_foo)
    transaction_b = transaction_factory(
        datetime.date.today() - datetime.timedelta(days=1)
    )
    transaction_a = transaction_factory(datetime.date.today())
    url = reverse("transactions:transaction_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["transaction_list"]) == [transaction_a, transaction_b]


def test_transaction_list_view_get_current_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    transaction_factory: Callable[..., Transaction],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    transaction_a = transaction_factory(user=user_a)
    transaction_factory(user=user_b)
    url = reverse("transactions:transaction_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["transaction_list"]) == [transaction_a]


def test_transaction_create_view_get(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("transactions:transaction_create")
    response = client.get(url)
    assert response.status_code == 200


def test_transaction_create_view_get_not_logged_in(client: Client) -> None:
    url = reverse("transactions:transaction_create")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_transaction_create_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo: Account,
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("transactions:transaction_create")
    data = {
        "date": datetime.date.today(),
        "amount": 100.0,
        "category": category_foo.id,
        "account": account_foo.id,
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "transaction_list"


def test_transaction_create_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo: Account,
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("transactions:transaction_create")
    data = {
        "date": datetime.date.today(),
        "amount": 100.0,
        "category": category_foo.id,
        "account": account_foo.id,
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Transaction was created successfully" in messages


def test_transaction_update_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    transaction_foo: Transaction,
) -> None:
    login_user(user_foo)
    url = reverse("transactions:transaction_update", kwargs={"pk": transaction_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_transaction_update_view_get_not_logged_in(
    client: Client, transaction_foo: Transaction
) -> None:
    url = reverse("transactions:transaction_update", kwargs={"pk": transaction_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_transaction_update_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    transaction_foo: Transaction,
    account_foo: Account,
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("transactions:transaction_update", kwargs={"pk": transaction_foo.pk})
    data = {
        "date": datetime.date.today(),
        "amount": 100.0,
        "category": category_foo.id,
        "account": account_foo.id,
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "transaction_list"


def test_transaction_update_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    transaction_foo: Transaction,
    account_foo: Account,
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("transactions:transaction_update", kwargs={"pk": transaction_foo.pk})
    data = {
        "date": datetime.date.today(),
        "amount": 100.0,
        "category": category_foo.id,
        "account": account_foo.id,
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Transaction was updated successfully" in messages


def test_transaction_update_view_post_different_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    transaction_factory: Callable[..., Transaction],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    transaction_factory(user=user_a)
    transaction_b = transaction_factory(user=user_b)
    url = reverse("transactions:transaction_update", kwargs={"pk": transaction_b.pk})
    data = {
        "description": "bx",
    }
    response = client.post(url, data=data)
    assert response.status_code == 403


def test_transaction_delete_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    transaction_foo: Transaction,
) -> None:
    login_user(user_foo)
    url = reverse("transactions:transaction_delete", kwargs={"pk": transaction_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_transaction_delete_view_get_not_logged_in(
    client: Client, transaction_foo: Transaction
) -> None:
    url = reverse("transactions:transaction_delete", kwargs={"pk": transaction_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_transaction_delete_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    transaction_foo: Transaction,
) -> None:
    login_user(user_foo)
    url = reverse("transactions:transaction_delete", kwargs={"pk": transaction_foo.pk})
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "transaction_list"


def test_transaction_delete_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    transaction_foo: Transaction,
) -> None:
    login_user(user_foo)
    url = reverse("transactions:transaction_delete", kwargs={"pk": transaction_foo.pk})
    response = client.post(url)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Transaction was deleted successfully" in messages


def test_transaction_delete_view_post_different_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    transaction_factory: Transaction,
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    transaction_factory(user=user_a)
    transaction_b = transaction_factory(user=user_b)
    url = reverse("transactions:transaction_delete", kwargs={"pk": transaction_b.pk})
    response = client.post(url)
    assert response.status_code == 403


def test_category_list_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    category_factory: Callable[..., Category],
) -> None:
    login_user(user_foo)
    categories = [
        category_factory("a"),
        category_factory("b"),
        category_factory("c"),
    ]
    url = reverse("categories:category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert len(response.context["category_list"]) == len(categories)


def test_category_list_view_get_not_logged_in(client: Client) -> None:
    url = reverse("categories:category_list")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_category_list_view_get_ordered_by_name(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    category_factory: Callable[..., Category],
) -> None:
    login_user(user_foo)
    category_factory("b")
    category_factory("a")
    url = reverse("categories:category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["category_list"]) == list(
        Category.objects.filter(user=user_foo).order_by("name")
    )


def test_category_list_view_get_current_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    category_factory: Callable[..., Category],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    category_factory("a", user=user_a)
    category_factory("b", user=user_b)
    url = reverse("categories:category_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["category_list"]) == list(
        Category.objects.filter(user=user_a).order_by("name")
    )


def test_category_create_view_get(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("categories:category_create")
    response = client.get(url)
    assert response.status_code == 200


def test_category_create_view_get_not_logged_in(client: Client) -> None:
    url = reverse("categories:category_create")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_category_create_view_post_redirect(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("categories:category_create")
    data = {
        "name": "a",
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "category_list"


def test_category_create_view_post_message(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("categories:category_create")
    data = {
        "name": "a",
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Category was created successfully" in messages


def test_category_update_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("categories:category_update", kwargs={"pk": category_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_category_update_view_get_not_logged_in(
    client: Client, category_foo: Category
) -> None:
    url = reverse("categories:category_update", kwargs={"pk": category_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_category_update_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("categories:category_update", kwargs={"pk": category_foo.pk})
    data = {
        "name": "bar",
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "category_list"


def test_category_update_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("categories:category_update", kwargs={"pk": category_foo.pk})
    data = {
        "name": "bar",
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Category was updated successfully" in messages


def test_category_update_view_post_different_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    category_factory: Callable[..., Category],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    category_factory("a", user=user_a)
    category_b = category_factory("b", user=user_b)
    url = reverse("categories:category_update", kwargs={"pk": category_b.pk})
    data = {"name": "bx", "category_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 403


def test_category_delete_view_get(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("categories:category_delete", kwargs={"pk": category_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_category_delete_view_get_not_logged_in(
    client: Client, category_foo: Category
) -> None:
    url = reverse("categories:category_delete", kwargs={"pk": category_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_category_delete_view_post_redirect(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("categories:category_delete", kwargs={"pk": category_foo.pk})
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "category_list"


def test_category_delete_view_post_message(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("categories:category_delete", kwargs={"pk": category_foo.pk})
    response = client.post(url)
    assert response.status_code == 302
    messages = [m.message for m in get_messages(response.wsgi_request)]
    assert "Category was deleted successfully" in messages


def test_category_delete_view_post_different_user(
    client: Client,
    user_factory: Callable[..., User],
    login_user: Callable[[User], None],
    category_factory: Callable[..., Category],
) -> None:
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    category_factory("a", user=user_a)
    category_b = category_factory("b", user=user_b)
    url = reverse("categories:category_delete", kwargs={"pk": category_b.pk})
    response = client.post(url)
    assert response.status_code == 403


def test_report_income_view_get(
    client: Client, user_foo: User, login_user: Callable[[User], None]
) -> None:
    login_user(user_foo)
    url = reverse("reports:report_income")
    response = client.get(url)
    assert response.status_code == 200


def test_report_income_view_get_not_logged_in(client: Client) -> None:
    url = reverse("reports:report_income")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_report_income_view_get_with_parameters(
    client: Client,
    user_foo: User,
    login_user: Callable[[User], None],
    account_foo: Account,
    category_foo: Category,
) -> None:
    login_user(user_foo)
    url = reverse("reports:report_income")
    data = {
        "accounts": [account_foo.pk],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
        "excluded_categories": [category_foo],
    }
    response = client.get(url, data)
    assert response.status_code == 200


def test_callback_success_new_connection(
    client: Client,
    profile_foo_external: Profile,
    mocker: MockFixture,
    saltedge_connection: saltedge_client.Connection,
) -> None:
    mocker.patch(
        "budget.views.get_connection", autospec=True, return_value=saltedge_connection
    )
    mocker.patch("budget.views.get_accounts", autospec=True, return_value=[])
    mocker.patch("budget.views.get_transactions", autospec=True, return_value=[])
    mocker.patch(
        "budget.views.get_pending_transactions", autospec=True, return_value=[]
    )
    mocker.patch("budget.views.verify_signature", autospec=True)

    url = reverse("callbacks:callback_success")
    data = {
        "data": {
            "connection_id": saltedge_connection.id,
            "customer_id": str(profile_foo_external.external_id),
            "custom_fields": {"key": "value"},
        },
        "meta": {"version": "5", "time": "2020-11-12T12:31:01.588Z"},
    }
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 204
    assert Connection.objects.filter(external_id=int(saltedge_connection.id)).exists()


def test_callback_success_new_account(
    client: Client,
    profile_foo_external: Profile,
    mocker: MockFixture,
    saltedge_connection: saltedge_client.Connection,
    saltedge_account: saltedge_client.Account,
) -> None:
    mocker.patch(
        "budget.views.get_connection", autospec=True, return_value=saltedge_connection
    )
    mocker.patch(
        "budget.views.get_accounts", autospec=True, return_value=[saltedge_account]
    )
    mocker.patch("budget.views.get_transactions", autospec=True, return_value=[])
    mocker.patch(
        "budget.views.get_pending_transactions", autospec=True, return_value=[]
    )
    mocker.patch("budget.views.verify_signature", autospec=True)

    url = reverse("callbacks:callback_success")
    data = {
        "data": {
            "connection_id": saltedge_connection.id,
            "customer_id": str(profile_foo_external.external_id),
            "custom_fields": {"key": "value"},
        },
        "meta": {"version": "5", "time": "2020-11-12T12:31:01.588Z"},
    }
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 204
    assert Account.objects.filter(external_id=int(saltedge_account.id)).exists()


def test_callback_success_new_transaction(
    client: Client,
    profile_foo_external: Profile,
    mocker: MockFixture,
    saltedge_connection: saltedge_client.Connection,
    saltedge_account: saltedge_client.Account,
    saltedge_transaction: saltedge_client.Transaction,
) -> None:
    mocker.patch(
        "budget.views.get_connection", autospec=True, return_value=saltedge_connection
    )
    mocker.patch(
        "budget.views.get_accounts", autospec=True, return_value=[saltedge_account]
    )
    mocker.patch(
        "budget.views.get_transactions",
        autospec=True,
        return_value=[saltedge_transaction],
    )
    mocker.patch(
        "budget.views.get_pending_transactions", autospec=True, return_value=[]
    )
    mocker.patch("budget.views.verify_signature", autospec=True)

    url = reverse("callbacks:callback_success")
    data = {
        "data": {
            "connection_id": saltedge_connection.id,
            "customer_id": str(profile_foo_external.external_id),
            "custom_fields": {"key": "value"},
        },
        "meta": {"version": "5", "time": "2020-11-12T12:31:01.588Z"},
    }
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 204
    assert Transaction.objects.filter(external_id=int(saltedge_transaction.id)).exists()


def test_callback_success_initial_balance(
    client: Client,
    profile_foo_external: Profile,
    mocker: MockFixture,
    saltedge_connection: saltedge_client.Connection,
    saltedge_account: saltedge_client.Account,
    saltedge_transaction: saltedge_client.Transaction,
) -> None:
    mocker.patch(
        "budget.views.get_connection", autospec=True, return_value=saltedge_connection
    )
    mocker.patch(
        "budget.views.get_accounts", autospec=True, return_value=[saltedge_account]
    )
    mocker.patch(
        "budget.views.get_transactions",
        autospec=True,
        return_value=[saltedge_transaction],
    )
    mocker.patch(
        "budget.views.get_pending_transactions",
        autospec=True,
        return_value=[saltedge_transaction],
    )
    mocker.patch("budget.views.verify_signature", autospec=True)

    url = reverse("callbacks:callback_success")
    data = {
        "data": {
            "connection_id": saltedge_connection.id,
            "customer_id": str(profile_foo_external.external_id),
            "custom_fields": {"key": "value"},
        },
        "meta": {"version": "5", "time": "2020-11-12T12:31:01.588Z"},
    }
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 204
    assert Transaction.objects.filter(description="Initial balance").exists()


@pytest.mark.django_db
def test_callback_success_invalid_customer(client: Client, mocker: MockFixture) -> None:
    url = reverse("callbacks:callback_success")
    data = {
        "data": {
            "connection_id": "1234",
            "customer_id": "5678",
            "custom_fields": {"key": "value"},
        },
        "meta": {"version": "5", "time": "2020-11-12T12:31:01.588Z"},
    }
    mocker.patch("budget.views.verify_signature", autospec=True)
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 400


def test_callback_fail(client: Client, mocker: MockFixture,) -> None:
    url = reverse("callbacks:callback_fail")
    data = {
        "data": {
            "connection_id": "111111111111111111",
            "customer_id": "222222222222222222",
            "custom_fields": {"key": "value"},
            "error_class": "InvalidCredentials",
            "error_message": "Invalid credentials.",
        },
        "meta": {"version": "5", "time": "2020-11-12T12:31:01.606Z"},
    }
    mocker.patch("budget.views.verify_signature", autospec=True)
    mocker.patch("budget.views.get_accounts", autospec=True, return_value=[])
    mocker.patch("budget.views.remove_connection_from_saltedge", autospec=True)
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 204


def test_callback_destroy(
    client: Client,
    profile_foo_external: Profile,
    connection_foo: Connection,
    mocker: MockFixture,
) -> None:
    url = reverse("callbacks:callback_destroy")
    data = {
        "data": {
            "connection_id": str(connection_foo.external_id),
            "customer_id": str(profile_foo_external.external_id),
        },
        "meta": {"version": "5", "time": "2020-11-11T12:31:01Z"},
    }
    mocker.patch("budget.views.verify_signature", autospec=True)
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 204
    assert not Connection.objects.filter(pk=connection_foo.pk).exists()


def test_callback_destroy_invalid_customer(
    client: Client, connection_foo: Connection, mocker: MockFixture
) -> None:
    url = reverse("callbacks:callback_destroy")
    data = {
        "data": {
            "connection_id": str(connection_foo.external_id),
            "customer_id": "1234",
        },
        "meta": {"version": "5", "time": "2020-11-11T12:31:01Z"},
    }
    mocker.patch("budget.views.verify_signature", autospec=True)
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 400


def test_callback_destroy_invalid_connection(
    client: Client, profile_foo_external: Profile, mocker: MockFixture
) -> None:
    url = reverse("callbacks:callback_destroy")
    data = {
        "data": {
            "connection_id": "1234",
            "customer_id": str(profile_foo_external.external_id),
        },
        "meta": {"version": "5", "time": "2020-11-11T12:31:01Z"},
    }
    mocker.patch("budget.views.verify_signature", autospec=True)
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 400


def test_callback_notify(client: Client, mocker: MockFixture) -> None:
    url = reverse("callbacks:callback_notify")
    data = {
        "data": {
            "connection_id": "111111111111111111",
            "customer_id": "222222222222222222",
            "custom_fields": {"key": "value"},
            "stage": "start",
        },
        "meta": {"version": "5", "time": "2020-11-11T12:31:01Z"},
    }
    mocker.patch("budget.views.verify_signature", autospec=True)
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 204


def test_callback_service(client: Client, mocker: MockFixture) -> None:
    url = reverse("callbacks:callback_service")
    data = {
        "data": {
            "connection_id": "111111111111111111",
            "customer_id": "222222222222222222",
            "custom_fields": {"key": "value"},
            "reason": "updated",
        },
        "meta": {"version": "5", "time": "2020-11-11T12:31:01Z"},
    }
    mocker.patch("budget.views.verify_signature", autospec=True)
    response = client.post(
        url, json.dumps(data), content_type="application/json", HTTP_SIGNATURE="TODO"
    )
    assert response.status_code == 204


def test_verify_signature_success() -> None:
    public_key_pem = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvL/Xxdmj7/cpZgvDMvxr
nTTU/vkHGM/qkJ0Q+rmfYLru0Z/rSWthPDEK3orY5BTa0sAe2wUV5Fes677X6+Ib
roCF8nODW5hSVTrqWcrQ55I7InpFkpTxyMkiFN8XPS7qmYXl/xofbYq0olcwE/aw
9lfHlZD7iwOpVJqTsYiXzSMRu92ZdECV895kYS/ggymSEtoMSW3405dQ6OfnK53x
7AJPdkAp0Wa2Lk4BNBMd24uu2tasO1bTYBsHpxonwbA+o8BXffdTEloloJgW7pV+
TWvxB/Uxil4yhZZJaFmvTCefxWFovyzLdjn2aSAEI7D1y4IYOdByMOPYQ6Mn7J9A
9wIDAQAB
-----END PUBLIC KEY-----
    """
    signature_base64 = "LhW+IftaENhUedrIsWp//ySu55XUs+e0seaJq7dFkiIGJH8XBF+z4yMYWCrr54MDIwwQV3WQ3BlJ6zq5SMiSt5cD72UFtV7dhMndfbKE51ItfpdAaGn47xXab3Nd5kAImNiOse6PUHknFh1mS/lSTF6jIePm6Gv5/BhVm8Y9O+ZBCy/A/GWXE49o6Ai+9StkTXj+6NAwNjvhyMEEBxJIB1d9MmfcrPvHhGV5F7WJxTHb3mNafapkkXO7Lp4dfa1902CzJUQUBt8kBd6dEZyk4NbUKQPOfi6I4HDpt4u+iELgI9M+vwzv8fwWzBpnvTfht1xbklKC3cYFMlaiQO54JQ=="
    data = 'http://budget-supervisor-stage.herokuapp.com/callbacks/success/|{"data":{"connection_id":"349600516445047165","customer_id":"345935467172071692","custom_fields":{}},"meta":{"version":"5","time":"2020-11-12T21:00:19.000Z"}}'

    verify_signature(public_key_pem, signature_base64, data)


def test_verify_signature_invalid_signature() -> None:
    public_key_pem = """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvL/Xxdmj7/cpZgvDMvxr
nTTU/vkHGM/qkJ0Q+rmfYLru0Z/rSWthPDEK3orY5BTa0sAe2wUV5Fes677X6+Ib
roCF8nODW5hSVTrqWcrQ55I7InpFkpTxyMkiFN8XPS7qmYXl/xofbYq0olcwE/aw
9lfHlZD7iwOpVJqTsYiXzSMRu92ZdECV895kYS/ggymSEtoMSW3405dQ6OfnK53x
7AJPdkAp0Wa2Lk4BNBMd24uu2tasO1bTYBsHpxonwbA+o8BXffdTEloloJgW7pV+
TWvxB/Uxil4yhZZJaFmvTCefxWFovyzLdjn2aSAEI7D1y4IYOdByMOPYQ6Mn7J9A
9wIDAQAB
-----END PUBLIC KEY-----
    """
    signature_base64 = base64.b64encode(b"xyz").decode("ascii")
    data = 'http://budget-supervisor-stage.herokuapp.com/callbacks/success/|{"data":{"connection_id":"349600516445047165","customer_id":"345935467172071692","custom_fields":{}},"meta":{"version":"5","time":"2020-11-12T21:00:19.000Z"}}'

    with pytest.raises(OpenSSL.crypto.Error):
        verify_signature(public_key_pem, signature_base64, data)
