import datetime

from budget.models import Account, Category
from django.urls import resolve, reverse
from swagger_client import ConnectSessionResponse, ConnectSessionResponseData
from utils import get_url_path


def test_index_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("budget_index")
    response = client.get(url)
    assert response.status_code == 200


def test_index_view_get_not_logged_in(client):
    url = reverse("budget_index")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_list_view_get_single_connection(
    client, user_foo, login_user, connection_foo
):
    login_user(user_foo)
    url = reverse("connections:connection_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["connection_list"]) == [connection_foo]


def test_connection_list_view_get_not_logged_in(client):
    url = reverse("connections:connection_list")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_list_view_get_multiple_connections(
    client, user_foo, login_user, connection_factory
):
    login_user(user_foo)
    connection_a = connection_factory("a")
    connection_b = connection_factory("b")
    url = reverse("connections:connection_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["connection_list"]) == [connection_a, connection_b]


def test_connection_list_view_get_ordered_by_provider(
    client, user_foo, login_user, connection_factory
):
    login_user(user_foo)
    connection_b = connection_factory("b")
    connection_a = connection_factory("a")
    url = reverse("connections:connection_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["connection_list"]) == [connection_a, connection_b]


def test_connection_list_view_get_current_user(
    client, user_factory, login_user, connection_factory
):
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    connection_a = connection_factory("a", user=user_a)
    connection_factory("b", user=user_b)
    url = reverse("connections:connection_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["connection_list"]) == [connection_a]


def test_connection_create_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("connections:connection_create")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["profile"] == user_foo.profile


def test_connection_create_view_get_not_logged_in(client):
    url = reverse("connections:connection_create")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_create_view_post(
    client, user_foo, login_user, mocker, connect_sessions_api
):
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


def test_connection_update_view_get(client, user_foo, login_user, connection_foo):
    login_user(user_foo)
    url = reverse("connections:connection_update", kwargs={"pk": connection_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_connection_update_view_get_not_logged_in(client, connection_foo):
    url = reverse("connections:connection_update", kwargs={"pk": connection_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_update_view_post(client, user_foo, login_user, connection_foo):
    login_user(user_foo)
    url = reverse("connections:connection_update", kwargs={"pk": connection_foo.pk})
    data = {
        "provider": "bar",
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "connection_list"


def test_connection_update_view_post_different_user(
    client, user_factory, login_user, connection_factory
):
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    connection_factory("a", user=user_a)
    connection_b = connection_factory("b", user=user_b)
    url = reverse("connections:connection_update", kwargs={"pk": connection_b.pk})
    data = {"name": "bx", "connection_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 403


def test_connection_delete_view_get(client, user_foo, login_user, connection_foo):
    login_user(user_foo)
    url = reverse("connections:connection_delete", kwargs={"pk": connection_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_connection_delete_view_get_not_logged_in(client, connection_foo):
    url = reverse("connections:connection_delete", kwargs={"pk": connection_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_delete_view_post(client, user_foo, login_user, connection_foo):
    login_user(user_foo)
    url = reverse("connections:connection_delete", kwargs={"pk": connection_foo.pk})
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "connection_list"


def test_connection_delete_view_post_external(
    client, user_foo, login_user, connection_foo_external, mocker, connections_api
):
    login_user(user_foo)
    url = reverse(
        "connections:connection_delete", kwargs={"pk": connection_foo_external.pk}
    )
    mocker.patch(
        "budget.views.connections_api", autospec=True, return_value=connections_api
    )
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "connection_list"


def test_connection_delete_view_post_different_user(
    client, user_factory, login_user, connection_factory
):
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    connection_factory("a", user=user_a)
    connection_b = connection_factory("b", user=user_b)
    url = reverse("connections:connection_delete", kwargs={"pk": connection_b.pk})
    response = client.post(url)
    assert response.status_code == 403


def test_connection_import_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("connections:connection_import")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["profile"] == user_foo.profile


def test_connection_import_view_get_not_logged_in(client):
    url = reverse("connections:connection_import")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_connection_import_view_post(
    client, user_foo, login_user, connection_foo, mocker, connections_api
):
    login_user(user_foo)
    url = reverse("connections:connection_import")
    data = {"connection": connection_foo.id}
    mocker.patch(
        "budget.views.connections_api", autospec=True, return_value=connections_api
    )
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "connection_list"


def test_account_list_view_get_single_account(
    client, user_foo, login_user, account_foo
):
    login_user(user_foo)
    url = reverse("accounts:account_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["account_list"]) == [account_foo]


def test_account_list_view_get_not_logged_in(client):
    url = reverse("accounts:account_list")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_account_list_view_get_multiple_accounts(
    client, user_foo, login_user, account_factory
):
    login_user(user_foo)
    account_a = account_factory("a")
    account_b = account_factory("b")
    url = reverse("accounts:account_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["account_list"]) == [account_a, account_b]


def test_account_list_view_get_ordered_by_name(
    client, user_foo, login_user, account_factory
):
    login_user(user_foo)
    account_b = account_factory("b")
    account_a = account_factory("a")
    url = reverse("accounts:account_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["account_list"]) == [account_a, account_b]


def test_account_list_view_get_current_user(
    client, user_factory, login_user, account_factory
):
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    account_a = account_factory("a", user=user_a)
    account_factory("b", user=user_b)
    url = reverse("accounts:account_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["account_list"]) == [account_a]


def test_account_create_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("accounts:account_create")
    response = client.get(url)
    assert response.status_code == 200


def test_account_create_view_get_not_logged_in(client):
    url = reverse("accounts:account_create")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_account_create_view_post(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("accounts:account_create")
    data = {"name": "a", "account_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "account_list"


def test_account_update_view_get(client, user_foo, login_user, account_foo):
    login_user(user_foo)
    url = reverse("accounts:account_update", kwargs={"pk": account_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_account_update_view_get_not_logged_in(client, account_foo):
    url = reverse("accounts:account_update", kwargs={"pk": account_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_account_update_view_post(client, user_foo, login_user, account_foo):
    login_user(user_foo)
    url = reverse("accounts:account_update", kwargs={"pk": account_foo.pk})
    data = {"name": "bar", "account_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "account_list"


def test_account_update_view_post_different_user(
    client, user_factory, login_user, account_factory
):
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    account_factory("a", user=user_a)
    account_b = account_factory("b", user=user_b)
    url = reverse("accounts:account_update", kwargs={"pk": account_b.pk})
    data = {"name": "bx", "account_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 403


def test_account_delete_view_get(client, user_foo, login_user, account_foo):
    login_user(user_foo)
    url = reverse("accounts:account_delete", kwargs={"pk": account_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_account_delete_view_get_not_logged_in(client, account_foo):
    url = reverse("accounts:account_delete", kwargs={"pk": account_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_account_delete_view_post(client, user_foo, login_user, account_foo):
    login_user(user_foo)
    url = reverse("accounts:account_delete", kwargs={"pk": account_foo.pk})
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "account_list"


def test_account_delete_view_post_different_user(
    client, user_factory, login_user, account_factory
):
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    account_factory("a", user=user_a)
    account_b = account_factory("b", user=user_b)
    url = reverse("accounts:account_delete", kwargs={"pk": account_b.pk})
    response = client.post(url)
    assert response.status_code == 403


def test_account_import_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("accounts:account_import")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["profile"] == user_foo.profile


def test_account_import_view_get_not_logged_in(client):
    url = reverse("accounts:account_import")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_account_import_view_post(
    client, user_foo, login_user, connection_foo, mocker, accounts_api
):
    login_user(user_foo)
    url = reverse("accounts:account_import")
    data = {"connection": connection_foo.id}
    mocker.patch("budget.views.accounts_api", autospec=True, return_value=accounts_api)
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "account_list"


def test_transaction_list_view_get_single_transaction(
    client, user_foo, login_user, transaction_foo
):
    login_user(user_foo)
    url = reverse("transactions:transaction_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["transaction_list"]) == [transaction_foo]


def test_transaction_list_view_get_not_logged_in(client):
    url = reverse("transactions:transaction_list")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_transaction_list_view_get_multiple_transactions(
    client, user_foo, login_user, transaction_factory
):
    login_user(user_foo)
    transaction_a = transaction_factory()
    transaction_b = transaction_factory()
    url = reverse("transactions:transaction_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["transaction_list"]) == [transaction_a, transaction_b]


def test_transaction_list_view_get_ordered_by_date(
    client, user_foo, login_user, transaction_factory
):
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
    client, user_factory, login_user, transaction_factory
):
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    transaction_a = transaction_factory(user=user_a)
    transaction_factory(user=user_b)
    url = reverse("transactions:transaction_list")
    response = client.get(url)
    assert response.status_code == 200
    assert list(response.context["transaction_list"]) == [transaction_a]


def test_transaction_create_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("transactions:transaction_create")
    response = client.get(url)
    assert response.status_code == 200


def test_transaction_create_view_get_not_logged_in(client):
    url = reverse("transactions:transaction_create")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_transaction_create_view_post(
    client, user_foo, login_user, account_foo, category_foo
):
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


def test_transaction_update_view_get(client, user_foo, login_user, transaction_foo):
    login_user(user_foo)
    url = reverse("transactions:transaction_update", kwargs={"pk": transaction_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_transaction_update_view_get_not_logged_in(client, transaction_foo):
    url = reverse("transactions:transaction_update", kwargs={"pk": transaction_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_transaction_update_view_post(
    client, user_foo, login_user, transaction_foo, account_foo, category_foo
):
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


def test_transaction_update_view_post_different_user(
    client, user_factory, login_user, transaction_factory
):
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


def test_transaction_delete_view_get(client, user_foo, login_user, transaction_foo):
    login_user(user_foo)
    url = reverse("transactions:transaction_delete", kwargs={"pk": transaction_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_transaction_delete_view_get_not_logged_in(client, transaction_foo):
    url = reverse("transactions:transaction_delete", kwargs={"pk": transaction_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_transaction_delete_view_post(client, user_foo, login_user, transaction_foo):
    login_user(user_foo)
    url = reverse("transactions:transaction_delete", kwargs={"pk": transaction_foo.pk})
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "transaction_list"


def test_transaction_delete_view_post_different_user(
    client, user_factory, login_user, transaction_factory
):
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    transaction_factory(user=user_a)
    transaction_b = transaction_factory(user=user_b)
    url = reverse("transactions:transaction_delete", kwargs={"pk": transaction_b.pk})
    response = client.post(url)
    assert response.status_code == 403


def test_transaction_import_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("transactions:transaction_import")
    response = client.get(url)
    assert response.status_code == 200
    assert response.context["profile"] == user_foo.profile


def test_transaction_import_view_get_not_logged_in(client):
    url = reverse("transactions:transaction_import")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_transaction_import_view_post(
    client, user_foo, login_user, account_foo_external, mocker, transactions_api
):
    login_user(user_foo)
    url = reverse("transactions:transaction_import")
    data = {"account": account_foo_external.id}
    mocker.patch(
        "budget.views.transactions_api", autospec=True, return_value=transactions_api
    )
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "transaction_list"


def test_category_list_view_get(client, user_foo, login_user, category_factory):
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


def test_category_list_view_get_not_logged_in(client):
    url = reverse("categories:category_list")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_category_list_view_get_ordered_by_name(
    client, user_foo, login_user, category_factory
):
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
    client, user_factory, login_user, category_factory
):
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


def test_category_create_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("categories:category_create")
    response = client.get(url)
    assert response.status_code == 200


def test_category_create_view_get_not_logged_in(client):
    url = reverse("categories:category_create")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_category_create_view_post(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("categories:category_create")
    data = {
        "name": "a",
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "category_list"


def test_category_update_view_get(client, user_foo, login_user, category_foo):
    login_user(user_foo)
    url = reverse("categories:category_update", kwargs={"pk": category_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_category_update_view_get_not_logged_in(client, category_foo):
    url = reverse("categories:category_update", kwargs={"pk": category_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_category_update_view_post(client, user_foo, login_user, category_foo):
    login_user(user_foo)
    url = reverse("categories:category_update", kwargs={"pk": category_foo.pk})
    data = {
        "name": "bar",
    }
    response = client.post(url, data=data)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "category_list"


def test_category_update_view_post_different_user(
    client, user_factory, login_user, category_factory
):
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    category_factory("a", user=user_a)
    category_b = category_factory("b", user=user_b)
    url = reverse("categories:category_update", kwargs={"pk": category_b.pk})
    data = {"name": "bx", "category_type": Account.AccountType.ACCOUNT}
    response = client.post(url, data=data)
    assert response.status_code == 403


def test_category_delete_view_get(client, user_foo, login_user, category_foo):
    login_user(user_foo)
    url = reverse("categories:category_delete", kwargs={"pk": category_foo.pk})
    response = client.get(url)
    assert response.status_code == 200


def test_category_delete_view_get_not_logged_in(client, category_foo):
    url = reverse("categories:category_delete", kwargs={"pk": category_foo.pk})
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_category_delete_view_post(client, user_foo, login_user, category_foo):
    login_user(user_foo)
    url = reverse("categories:category_delete", kwargs={"pk": category_foo.pk})
    response = client.post(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "category_list"


def test_category_delete_view_post_different_user(
    client, user_factory, login_user, category_factory
):
    user_a = user_factory("a")
    user_b = user_factory("b")
    login_user(user_a)
    category_factory("a", user=user_a)
    category_b = category_factory("b", user=user_b)
    url = reverse("categories:category_delete", kwargs={"pk": category_b.pk})
    response = client.post(url)
    assert response.status_code == 403


def test_report_balance_view_get(client, user_foo, login_user):
    login_user(user_foo)
    url = reverse("reports:report_balance")
    response = client.get(url)
    assert response.status_code == 200


def test_report_balance_view_get_not_logged_in(client):
    url = reverse("reports:report_balance")
    response = client.get(url)
    assert response.status_code == 302
    assert resolve(get_url_path(response)).url_name == "login"


def test_report_balance_view_get_with_parameters(
    client, user_foo, login_user, account_foo
):
    login_user(user_foo)
    url = reverse("reports:report_balance")
    data = {
        "accounts": [account_foo.pk],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    response = client.get(url, data)
    assert response.status_code == 200
