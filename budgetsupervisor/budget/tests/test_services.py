import datetime
from typing import Callable

import swagger_client as saltedge_client
from budget.models import Account, Category, Connection, Transaction
from budget.services import (
    create_connection_in_saltedge,
    get_category_balance,
    import_accounts_from_saltedge,
    import_connections_from_saltedge,
    import_transactions_from_saltedge,
    remove_connection_from_saltedge,
)
from django.utils.dateparse import parse_date
from users.models import Profile, User


def test_create_connection_in_saltedge(
    profile_foo_external: Profile,
    connect_sessions_api: saltedge_client.ConnectSessionsApi,
) -> None:
    data = saltedge_client.ConnectSessionResponseData(connect_url="example.com")
    connect_sessions_api.connect_sessions_create_post.return_value = saltedge_client.ConnectSessionResponse(
        data=data
    )

    connect_url = create_connection_in_saltedge(
        "redirect_url", profile_foo_external.external_id, connect_sessions_api
    )
    assert connect_url == data.connect_url


def test_import_connections_from_saltedge_no_objects(
    profile_foo_external: Profile, connections_api: saltedge_client.ConnectionsApi
) -> None:
    connections_api.connections_get.return_value = saltedge_client.ConnectionsResponse(
        data=[]
    )

    assert Connection.objects.all().count() == 0
    imported_connections = import_connections_from_saltedge(
        profile_foo_external.user, profile_foo_external.external_id, connections_api
    )
    assert Connection.objects.all().count() == 0
    assert len(imported_connections) == 0


def test_import_connections_from_saltedge_one_new_object(
    profile_foo_external: Profile,
    connections_api: saltedge_client.ConnectionsApi,
    saltedge_connection_factory: Callable[..., saltedge_client.Connection],
) -> None:
    mock_connections = [saltedge_connection_factory(id="1", provider_name="foo")]
    connections_api.connections_get.return_value = saltedge_client.ConnectionsResponse(
        data=mock_connections
    )

    assert Connection.objects.all().count() == 0
    imported_connections = import_connections_from_saltedge(
        profile_foo_external.user, profile_foo_external.external_id, connections_api
    )
    assert Connection.objects.all().count() == len(mock_connections)
    assert len(imported_connections) == len(mock_connections)

    for imported, mock in zip(imported_connections, mock_connections):
        assert imported.external_id == int(mock.id)
        assert imported.provider == mock.provider_name
        assert imported.user == profile_foo_external.user


def test_import_connections_from_saltedge_two_new_objects(
    profile_foo_external: Profile,
    connections_api: saltedge_client.ConnectionsApi,
    saltedge_connection_factory: Callable[..., saltedge_client.Connection],
) -> None:
    mock_connections = [
        saltedge_connection_factory(id="1", provider_name="foo"),
        saltedge_connection_factory(id="2", provider_name="bar"),
    ]
    connections_api.connections_get.return_value = saltedge_client.ConnectionsResponse(
        data=mock_connections
    )

    assert Connection.objects.all().count() == 0
    imported_connections = import_connections_from_saltedge(
        profile_foo_external.user, profile_foo_external.external_id, connections_api
    )
    assert Connection.objects.all().count() == len(mock_connections)
    assert len(imported_connections) == len(mock_connections)

    for imported, mock in zip(imported_connections, mock_connections):
        assert imported.external_id == int(mock.id)
        assert imported.provider == mock.provider_name
        assert imported.user == profile_foo_external.user


def test_import_connections_from_saltedge_no_new_objects(
    profile_foo_external: Profile,
    connections_api: saltedge_client.ConnectionsApi,
    saltedge_connection_factory: Callable[..., saltedge_client.Connection],
) -> None:
    mock_connections = [
        saltedge_connection_factory(id="1"),
        saltedge_connection_factory(id="2"),
    ]
    connections_api.connections_get.return_value = saltedge_client.ConnectionsResponse(
        data=mock_connections
    )
    imported_connections = import_connections_from_saltedge(
        profile_foo_external.user, profile_foo_external.external_id, connections_api
    )

    assert Connection.objects.all().count() == len(mock_connections)
    imported_connections = import_connections_from_saltedge(
        profile_foo_external.user, profile_foo_external.external_id, connections_api
    )
    assert Connection.objects.all().count() == len(mock_connections)
    assert len(imported_connections) == 0


def test_remove_connection_saltedge(
    connection_foo: Connection, connections_api: saltedge_client.ConnectionsApi
) -> None:
    data = saltedge_client.RemovedConnectionResponseData(
        removed=True, id=str(connection_foo.external_id)
    )
    connections_api.connections_connection_id_delete.return_value = saltedge_client.RemovedConnectionResponse(
        data=data
    )

    remove_connection_from_saltedge(connection_foo, connections_api)
    connections_api.connections_connection_id_delete.assert_called_with(
        str(connection_foo.external_id)
    )


def test_import_accounts_from_saltedge_no_objects(
    connection_foo: Connection, accounts_api: saltedge_client.AccountsApi
) -> None:
    accounts_api.accounts_get.return_value = saltedge_client.AccountsResponse(data=[])

    assert Account.objects.all().count() == 0
    imported_accounts = import_accounts_from_saltedge(
        connection_foo.user, connection_foo.external_id, accounts_api
    )
    assert Account.objects.all().count() == 0
    assert len(imported_accounts) == 0


def test_import_accounts_from_saltedge_one_new_object(
    connection_foo: Connection,
    accounts_api: saltedge_client.AccountsApi,
    saltedge_account_factory: Callable[..., saltedge_client.Account],
) -> None:
    mock_accounts = [saltedge_account_factory(id="1", name="foo")]
    accounts_api.accounts_get.return_value = saltedge_client.AccountsResponse(
        data=mock_accounts
    )

    assert Account.objects.all().count() == 0
    imported_accounts = import_accounts_from_saltedge(
        connection_foo.user, connection_foo.external_id, accounts_api
    )
    assert Account.objects.all().count() == len(mock_accounts)
    assert len(imported_accounts) == len(mock_accounts)

    for imported, mock in zip(imported_accounts, mock_accounts):
        assert imported.external_id == int(mock.id)
        assert imported.name == mock.name
        assert imported.account_type == Account.AccountType.ACCOUNT
        assert imported.connection == connection_foo
        assert imported.user == connection_foo.user


def test_import_accounts_from_saltedge_two_new_objects(
    connection_foo: Connection,
    accounts_api: saltedge_client.AccountsApi,
    saltedge_account_factory: Callable[..., saltedge_client.Account],
) -> None:
    mock_accounts = [
        saltedge_account_factory(id="1", name="foo"),
        saltedge_account_factory(id="2", name="bar"),
    ]
    accounts_api.accounts_get.return_value = saltedge_client.AccountsResponse(
        data=mock_accounts
    )

    assert Account.objects.all().count() == 0
    imported_accounts = import_accounts_from_saltedge(
        connection_foo.user, connection_foo.external_id, accounts_api
    )
    assert Account.objects.all().count() == len(mock_accounts)
    assert len(imported_accounts) == len(mock_accounts)

    for imported, mock in zip(imported_accounts, mock_accounts):
        assert imported.external_id == int(mock.id)
        assert imported.name == mock.name
        assert imported.account_type == Account.AccountType.ACCOUNT
        assert imported.connection == connection_foo
        assert imported.user == connection_foo.user


def test_import_accounts_from_saltedge_no_new_objects(
    connection_foo: Connection,
    accounts_api: saltedge_client.AccountsApi,
    saltedge_account_factory: Callable[..., saltedge_client.Account],
) -> None:
    mock_accounts = [
        saltedge_account_factory(id="1"),
        saltedge_account_factory(id="2"),
    ]
    accounts_api.accounts_get.return_value = saltedge_client.AccountsResponse(
        data=mock_accounts
    )
    imported_accounts = import_accounts_from_saltedge(
        connection_foo.user, connection_foo.external_id, accounts_api
    )

    assert Account.objects.all().count() == len(mock_accounts)
    imported_accounts = import_accounts_from_saltedge(
        connection_foo.user, connection_foo.external_id, accounts_api
    )
    assert Account.objects.all().count() == len(mock_accounts)
    assert len(imported_accounts) == 0


def test_transaction_category_is_set_to_null_when_category_is_deleted(
    transaction_factory: Callable[..., Transaction], category_foo: Category
) -> None:
    transaction = transaction_factory(category=category_foo)
    category_foo.delete()
    transaction.refresh_from_db()
    assert transaction.category is None


def test_import_transactions_from_saltedge_no_objects(
    account_foo_external: Account, transactions_api: saltedge_client.TransactionsApi
) -> None:
    transactions_api.transactions_get.return_value = saltedge_client.TransactionsResponse(
        data=[]
    )

    assert Transaction.objects.all().count() == 0
    imported_transactions = import_transactions_from_saltedge(
        account_foo_external.user,
        account_foo_external.connection.external_id,
        account_foo_external.external_id,
        transactions_api,
    )
    assert Transaction.objects.all().count() == 0
    assert len(imported_transactions) == 0


def test_import_transactions_from_saltedge_one_new_object(
    account_foo_external: Account,
    transactions_api: saltedge_client.TransactionsApi,
    saltedge_transaction_factory: Callable[..., saltedge_client.Transaction],
) -> None:
    mock_transactions = [
        saltedge_transaction_factory(
            id="1",
            description="foo",
            amount=20.2,
            made_on=parse_date("2020-05-03"),
            account_id=account_foo_external.external_id,
        ),
    ]
    transactions_api.transactions_get.return_value = saltedge_client.TransactionsResponse(
        data=mock_transactions
    )

    assert Transaction.objects.all().count() == 0
    imported_transactions = import_transactions_from_saltedge(
        account_foo_external.user,
        account_foo_external.connection.external_id,
        account_foo_external.external_id,
        transactions_api,
    )
    assert Transaction.objects.all().count() == len(mock_transactions)
    assert len(imported_transactions) == len(mock_transactions)

    for imported, mock in zip(imported_transactions, mock_transactions):
        assert imported.external_id == int(mock.id)
        assert imported.date == mock.made_on
        assert imported.payee == ""
        assert imported.category is None
        assert imported.description == mock.description
        assert imported.account == account_foo_external
        assert imported.user == account_foo_external.user


def test_import_transactions_from_saltedge_two_new_objects(
    account_foo_external: Account,
    transactions_api: saltedge_client.TransactionsApi,
    saltedge_transaction_factory: Callable[..., saltedge_client.Transaction],
) -> None:
    mock_transactions = [
        saltedge_transaction_factory(
            id="1",
            description="foo",
            amount=20.2,
            made_on=parse_date("2020-05-03"),
            account_id=account_foo_external.external_id,
        ),
        saltedge_transaction_factory(
            id="2",
            description="bar",
            amount=-30.5,
            made_on=parse_date("2020-05-04"),
            account_id=account_foo_external.external_id,
        ),
    ]
    transactions_api.transactions_get.return_value = saltedge_client.TransactionsResponse(
        data=mock_transactions
    )

    assert Transaction.objects.all().count() == 0
    imported_transactions = import_transactions_from_saltedge(
        account_foo_external.user,
        account_foo_external.connection.external_id,
        account_foo_external.external_id,
        transactions_api,
    )
    assert Transaction.objects.all().count() == len(mock_transactions)
    assert len(imported_transactions) == len(mock_transactions)

    for imported, mock in zip(imported_transactions, mock_transactions):
        assert imported.external_id == int(mock.id)
        assert imported.date == mock.made_on
        assert imported.payee == ""
        assert imported.category is None
        assert imported.description == mock.description
        assert imported.account == account_foo_external
        assert imported.user == account_foo_external.user


def test_import_transactions_from_saltedge_no_new_objects(
    account_foo_external: Account,
    transactions_api: saltedge_client.TransactionsApi,
    saltedge_transaction_factory: Callable[..., saltedge_client.Transaction],
) -> None:
    mock_transactions = [
        saltedge_transaction_factory(
            id="1", account_id=account_foo_external.external_id
        ),
        saltedge_transaction_factory(
            id="2", account_id=account_foo_external.external_id
        ),
    ]
    transactions_api.transactions_get.return_value = saltedge_client.TransactionsResponse(
        data=mock_transactions
    )
    imported_transactions = import_transactions_from_saltedge(
        account_foo_external.user,
        account_foo_external.connection.external_id,
        account_foo_external.external_id,
        transactions_api,
    )

    assert Transaction.objects.all().count() == len(mock_transactions)
    imported_transactions = import_transactions_from_saltedge(
        account_foo_external.user,
        account_foo_external.connection.external_id,
        account_foo_external.external_id,
        transactions_api,
    )
    assert Transaction.objects.all().count() == len(mock_transactions)
    assert len(imported_transactions) == 0


def test_get_category_balance_filter_by_user(
    user_factory: Callable[..., User],
    account_factory: Callable[..., Account],
    category_factory: Callable[..., Category],
    transaction_factory: Callable[..., Transaction],
) -> None:
    user_abc = user_factory("abc")
    user_xyz = user_factory("xyz")

    account_abc = account_factory("abc", user=user_abc)
    account_xyz = account_factory("xyz", user=user_xyz)

    category_abc = category_factory("abc", user_abc)
    category_xyz = category_factory("xyz", user_xyz)

    transaction_factory(
        amount=123.00, account=account_abc, user=user_abc, category=category_abc
    )
    transaction_factory(
        amount=256.00, account=account_xyz, user=user_xyz, category=category_xyz
    )

    output = get_category_balance(accounts=[account_abc, account_xyz], user=user_abc,)

    assert output == {"abc": 123.00, "Total": 123.00}


def test_get_category_balance_filter_by_account(
    user_factory: Callable[..., User],
    account_factory: Callable[..., Account],
    category_factory: Callable[..., Category],
    transaction_factory: Callable[..., Transaction],
) -> None:
    user_abc = user_factory("abc")

    account_abc_1 = account_factory("abc_1", user=user_abc)
    account_abc_2 = account_factory("abc_2", user=user_abc)
    account_abc_3 = account_factory("abc_3", user=user_abc)

    category_abc = category_factory("abc", user_abc)

    transaction_factory(
        amount=4.00, account=account_abc_1, user=user_abc, category=category_abc
    )
    transaction_factory(
        amount=5.00, account=account_abc_2, user=user_abc, category=category_abc
    )
    transaction_factory(
        amount=6.00, account=account_abc_3, user=user_abc, category=category_abc
    )

    output = get_category_balance(
        accounts=[account_abc_1, account_abc_2], user=user_abc,
    )

    assert output == {"abc": 4.00 + 5.00, "Total": 4.00 + 5.00}


def test_get_category_balance_per_category(
    user_factory: Callable[..., User],
    account_factory: Callable[..., Account],
    category_factory: Callable[..., Category],
    transaction_factory: Callable[..., Transaction],
) -> None:
    user_abc = user_factory("abc")
    account_abc = account_factory("abc", user=user_abc)
    category_abc_1 = category_factory("abc_1", user_abc)
    category_abc_2 = category_factory("abc_2", user_abc)

    transaction_factory(
        amount=4.00, account=account_abc, user=user_abc, category=category_abc_1
    )
    transaction_factory(
        amount=5.00, account=account_abc, user=user_abc, category=category_abc_2
    )

    output = get_category_balance(accounts=[account_abc], user=user_abc,)

    assert output == {"abc_1": 4.00, "abc_2": 5.00, "Total": 4.00 + 5.00}


def test_get_category_balance_filter_by_from_date(
    user_factory: Callable[..., User],
    account_factory: Callable[..., Account],
    category_factory: Callable[..., Category],
    transaction_factory: Callable[..., Transaction],
) -> None:
    user_abc = user_factory("abc")
    account_abc = account_factory("abc", user=user_abc)
    category_abc = category_factory("abc", user_abc)

    transaction_factory(
        amount=4.00,
        account=account_abc,
        date=datetime.date(2020, 2, 1),
        user=user_abc,
        category=category_abc,
    )
    transaction_factory(
        amount=5.00,
        account=account_abc,
        date=datetime.date(2020, 3, 1),
        user=user_abc,
        category=category_abc,
    )
    transaction_factory(
        amount=6.00,
        account=account_abc,
        date=datetime.date(2020, 4, 1),
        user=user_abc,
        category=category_abc,
    )

    output = get_category_balance(
        accounts=[account_abc], user=user_abc, from_date=datetime.date(2020, 3, 1)
    )

    assert output == {"abc": 5.00 + 6.00, "Total": 5.00 + 6.00}


def test_get_category_balance_filter_by_to_date(
    user_factory: Callable[..., User],
    account_factory: Callable[..., Account],
    category_factory: Callable[..., Category],
    transaction_factory: Callable[..., Transaction],
) -> None:
    user_abc = user_factory("abc")
    account_abc = account_factory("abc", user=user_abc)
    category_abc = category_factory("abc", user_abc)

    transaction_factory(
        amount=4.00,
        account=account_abc,
        date=datetime.date(2020, 2, 1),
        user=user_abc,
        category=category_abc,
    )
    transaction_factory(
        amount=5.00,
        account=account_abc,
        date=datetime.date(2020, 3, 1),
        user=user_abc,
        category=category_abc,
    )
    transaction_factory(
        amount=6.00,
        account=account_abc,
        date=datetime.date(2020, 4, 1),
        user=user_abc,
        category=category_abc,
    )

    output = get_category_balance(
        accounts=[account_abc], user=user_abc, to_date=datetime.date(2020, 3, 1)
    )

    assert output == {"abc": 4.00 + 5.00, "Total": 4.00 + 5.00}
