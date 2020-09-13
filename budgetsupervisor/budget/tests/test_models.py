from budget.models import Connection, Account, Category, Transaction
import pytest
import datetime
import swagger_client as saltedge_client


@pytest.fixture
def connection_factory(db, user_foo):
    def create_connection(
        provider, user=user_foo, external_id=None,
    ):
        return Connection.objects.create(
            provider=provider, user=user, external_id=external_id
        )

    return create_connection


@pytest.fixture
def connection_foo(connection_factory):
    return connection_factory("foo")


@pytest.fixture
def connection_foo_external(connection_factory, profile_foo_external):
    return connection_factory(
        provider="foo", user=profile_foo_external.user, external_id=123
    )


def test_connection_str(connection_foo):
    assert str(connection_foo) == "foo"


def test_connection_create_in_saltedge(profile_foo_external, connect_sessions_api):
    data = saltedge_client.ConnectSessionResponseData(connect_url="foo.com")
    connect_sessions_api.connect_sessions_create_post.return_value = saltedge_client.ConnectSessionResponse(
        data=data
    )

    connect_url = Connection.objects.create_in_saltedge(
        "redirect_url", profile_foo_external.external_id, connect_sessions_api
    )
    assert connect_url == data.connect_url


def test_connection_import_from_saltedge_no_objects(
    profile_foo_external, connections_api
):
    connections_api.connections_get.return_value = saltedge_client.ConnectionsResponse(
        data=[]
    )

    assert Connection.objects.all().count() == 0
    imported_connections = Connection.objects.import_from_saltedge(
        profile_foo_external.user, profile_foo_external.external_id, connections_api
    )
    assert Connection.objects.all().count() == 0
    assert len(imported_connections) == 0


def test_connection_import_from_saltedge_one_new_object(
    profile_foo_external, connections_api, saltedge_connection_factory
):
    mock_connections = [saltedge_connection_factory(id="1", provider_name="foo")]
    connections_api.connections_get.return_value = saltedge_client.ConnectionsResponse(
        data=mock_connections
    )

    assert Connection.objects.all().count() == 0
    imported_connections = Connection.objects.import_from_saltedge(
        profile_foo_external.user, profile_foo_external.external_id, connections_api
    )
    assert Connection.objects.all().count() == len(mock_connections)
    assert len(imported_connections) == len(mock_connections)

    for imported, mock in zip(imported_connections, mock_connections):
        assert imported.external_id == int(mock.id)
        assert imported.provider == mock.provider_name
        assert imported.user == profile_foo_external.user


def test_connection_import_from_saltedge_two_new_objects(
    profile_foo_external, connections_api, saltedge_connection_factory
):
    mock_connections = [
        saltedge_connection_factory(id="1", provider_name="foo"),
        saltedge_connection_factory(id="2", provider_name="bar"),
    ]
    connections_api.connections_get.return_value = saltedge_client.ConnectionsResponse(
        data=mock_connections
    )

    assert Connection.objects.all().count() == 0
    imported_connections = Connection.objects.import_from_saltedge(
        profile_foo_external.user, profile_foo_external.external_id, connections_api
    )
    assert Connection.objects.all().count() == len(mock_connections)
    assert len(imported_connections) == len(mock_connections)

    for imported, mock in zip(imported_connections, mock_connections):
        assert imported.external_id == int(mock.id)
        assert imported.provider == mock.provider_name
        assert imported.user == profile_foo_external.user


def test_connection_import_from_saltedge_no_new_objects(
    profile_foo_external, connections_api, saltedge_connection_factory
):
    mock_connections = [
        saltedge_connection_factory(id="1"),
        saltedge_connection_factory(id="2"),
    ]
    connections_api.connections_get.return_value = saltedge_client.ConnectionsResponse(
        data=mock_connections
    )
    imported_connections = Connection.objects.import_from_saltedge(
        profile_foo_external.user, profile_foo_external.external_id, connections_api
    )

    assert Connection.objects.all().count() == len(mock_connections)
    imported_connections = Connection.objects.import_from_saltedge(
        profile_foo_external.user, profile_foo_external.external_id, connections_api
    )
    assert Connection.objects.all().count() == len(mock_connections)
    assert len(imported_connections) == 0


def test_connection_remove_saltedge(connection_foo_external, connections_api):
    data = saltedge_client.RemovedConnectionResponseData(
        removed=True, id=str(connection_foo_external.external_id)
    )
    connections_api.connections_connection_id_delete.return_value = saltedge_client.RemovedConnectionResponse(
        data=data
    )

    assert connection_foo_external.external_id is not None
    Connection.objects.remove_from_saltedge(connection_foo_external, connections_api)
    assert connection_foo_external.external_id is None


@pytest.fixture
def account_factory(db, connection_foo, user_foo):
    def create_account(
        name,
        account_type=Account.AccountType.ACCOUNT,
        external_id=None,
        connection=connection_foo,
        user=user_foo,
    ):
        return Account.objects.create(
            name=name,
            account_type=account_type,
            external_id=external_id,
            connection=connection,
            user=user,
        )

    return create_account


@pytest.fixture
def account_foo(account_factory):
    return account_factory("foo")


@pytest.fixture
def account_foo_external(account_factory, connection_foo_external):
    return account_factory("foo", external_id=123, connection=connection_foo_external)


def test_account_str(account_foo):
    assert str(account_foo) == "foo"


def test_account_import_from_saltedge_no_objects(connection_foo_external, accounts_api):
    accounts_api.accounts_get.return_value = saltedge_client.AccountsResponse(data=[])

    assert Account.objects.all().count() == 0
    imported_accounts = Account.objects.import_from_saltedge(
        connection_foo_external.user, connection_foo_external.external_id, accounts_api
    )
    assert Account.objects.all().count() == 0
    assert len(imported_accounts) == 0


def test_account_import_from_saltedge_one_new_object(
    connection_foo_external, accounts_api, saltedge_account_factory
):
    mock_accounts = [saltedge_account_factory(id="1", name="foo")]
    accounts_api.accounts_get.return_value = saltedge_client.AccountsResponse(
        data=mock_accounts
    )

    assert Account.objects.all().count() == 0
    imported_accounts = Account.objects.import_from_saltedge(
        connection_foo_external.user, connection_foo_external.external_id, accounts_api
    )
    assert Account.objects.all().count() == len(mock_accounts)
    assert len(imported_accounts) == len(mock_accounts)

    for imported, mock in zip(imported_accounts, mock_accounts):
        assert imported.external_id == int(mock.id)
        assert imported.name == mock.name
        assert imported.account_type == Account.AccountType.ACCOUNT
        assert imported.connection == connection_foo_external
        assert imported.user == connection_foo_external.user


def test_account_import_from_saltedge_two_new_objects(
    connection_foo_external, accounts_api, saltedge_account_factory
):
    mock_accounts = [
        saltedge_account_factory(id="1", name="foo"),
        saltedge_account_factory(id="2", name="bar"),
    ]
    accounts_api.accounts_get.return_value = saltedge_client.AccountsResponse(
        data=mock_accounts
    )

    assert Account.objects.all().count() == 0
    imported_accounts = Account.objects.import_from_saltedge(
        connection_foo_external.user, connection_foo_external.external_id, accounts_api
    )
    assert Account.objects.all().count() == len(mock_accounts)
    assert len(imported_accounts) == len(mock_accounts)

    for imported, mock in zip(imported_accounts, mock_accounts):
        assert imported.external_id == int(mock.id)
        assert imported.name == mock.name
        assert imported.account_type == Account.AccountType.ACCOUNT
        assert imported.connection == connection_foo_external
        assert imported.user == connection_foo_external.user


def test_account_import_from_saltedge_no_new_objects(
    connection_foo_external, accounts_api, saltedge_account_factory
):
    mock_accounts = [
        saltedge_account_factory(id="1"),
        saltedge_account_factory(id="2"),
    ]
    accounts_api.accounts_get.return_value = saltedge_client.AccountsResponse(
        data=mock_accounts
    )
    imported_accounts = Account.objects.import_from_saltedge(
        connection_foo_external.user, connection_foo_external.external_id, accounts_api
    )

    assert Account.objects.all().count() == len(mock_accounts)
    imported_accounts = Account.objects.import_from_saltedge(
        connection_foo_external.user, connection_foo_external.external_id, accounts_api
    )
    assert Account.objects.all().count() == len(mock_accounts)
    assert len(imported_accounts) == 0


@pytest.fixture
def category_factory(db, user_foo):
    def create_category(name, user=user_foo):
        return Category.objects.create(name=name, user=user)

    return create_category


@pytest.fixture
def category_foo(category_factory):
    return category_factory("foo")


def test_category_str(category_foo):
    assert str(category_foo) == "foo"


def test_categories_are_populated_after_user_is_created(db, user_foo):
    expected_categories = [
        "Auto and Transport",
        "Bills and Utilities",
        "Education",
        "Entertainment",
        "Fees and Charges",
        "Food and Dining",
        "Gifts and Donations",
        "Health and Fitness",
        "Home",
        "Income",
        "Insurance",
        "Kids",
        "Pets",
        "Shopping",
        "Transfer",
        "Travel",
        "Uncategorized",
    ]
    for category in expected_categories:
        assert Category.objects.filter(user=user_foo, name=category).exists()


@pytest.fixture
def transaction_factory(db, account_foo, category_foo, user_foo):
    def create_transaction(
        date=datetime.date.today(),
        amount=100.00,
        payee="",
        category=category_foo,
        description="",
        account=account_foo,
        external_id=None,
        user=user_foo,
    ):
        return Transaction.objects.create(
            date=date,
            amount=amount,
            payee=payee,
            category=category,
            description=description,
            account=account,
            external_id=None,
            user=user,
        )

    return create_transaction


@pytest.fixture
def transaction_foo(transaction_factory):
    return transaction_factory()


@pytest.fixture
def transaction_foo_external(transaction_factory):
    return transaction_factory(external_id=123)


def test_transaction_str(transaction_foo):
    assert str(transaction_foo) == "1"


def test_transaction_import_from_saltedge_no_objects(
    account_foo_external, transactions_api
):
    transactions_api.transactions_get.return_value = saltedge_client.TransactionsResponse(
        data=[]
    )

    assert Transaction.objects.all().count() == 0
    imported_transactions = Transaction.objects.import_from_saltedge(
        account_foo_external.user,
        account_foo_external.connection.external_id,
        account_foo_external.external_id,
        transactions_api,
    )
    assert Transaction.objects.all().count() == 0
    assert len(imported_transactions) == 0


def test_transaction_import_from_saltedge_one_new_object(
    account_foo_external, transactions_api, saltedge_transaction_factory
):
    mock_transactions = [
        saltedge_transaction_factory(
            id="1",
            description="foo",
            amount=20.2,
            made_on="2020-05-03",
            account_id=account_foo_external.external_id,
        ),
    ]
    transactions_api.transactions_get.return_value = saltedge_client.TransactionsResponse(
        data=mock_transactions
    )

    assert Transaction.objects.all().count() == 0
    imported_transactions = Transaction.objects.import_from_saltedge(
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
        assert (
            imported.category
            == Category.objects.filter(
                name__iexact=mock.category, user=account_foo_external.user
            )[0]
        )
        assert imported.description == mock.description
        assert imported.account == account_foo_external
        assert imported.user == account_foo_external.user


def test_transaction_import_from_saltedge_two_new_objects(
    account_foo_external, transactions_api, saltedge_transaction_factory
):
    mock_transactions = [
        saltedge_transaction_factory(
            id="1",
            description="foo",
            amount=20.2,
            made_on="2020-05-03",
            account_id=account_foo_external.external_id,
        ),
        saltedge_transaction_factory(
            id="2",
            description="bar",
            amount=-30.5,
            made_on="2020-05-04",
            account_id=account_foo_external.external_id,
        ),
    ]
    transactions_api.transactions_get.return_value = saltedge_client.TransactionsResponse(
        data=mock_transactions
    )

    assert Transaction.objects.all().count() == 0
    imported_transactions = Transaction.objects.import_from_saltedge(
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
        assert (
            imported.category
            == Category.objects.filter(
                name__iexact=mock.category, user=account_foo_external.user
            )[0]
        )
        assert imported.description == mock.description
        assert imported.account == account_foo_external
        assert imported.user == account_foo_external.user


def test_transaction_import_from_saltedge_no_new_objects(
    account_foo_external, transactions_api, saltedge_transaction_factory
):
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
    imported_transactions = Transaction.objects.import_from_saltedge(
        account_foo_external.user,
        account_foo_external.connection.external_id,
        account_foo_external.external_id,
        transactions_api,
    )

    assert Transaction.objects.all().count() == len(mock_transactions)
    imported_transactions = Transaction.objects.import_from_saltedge(
        account_foo_external.user,
        account_foo_external.connection.external_id,
        account_foo_external.external_id,
        transactions_api,
    )
    assert Transaction.objects.all().count() == len(mock_transactions)
    assert len(imported_transactions) == 0


def test_transaction_import_from_saltedge_category_with_spaces(
    account_foo_external, transactions_api, saltedge_transaction_factory
):
    mock_transactions = [
        saltedge_transaction_factory(
            id="1",
            category="fees_and_charges",
            account_id=account_foo_external.external_id,
        ),
    ]
    transactions_api.transactions_get.return_value = saltedge_client.TransactionsResponse(
        data=mock_transactions
    )

    imported_transactions = Transaction.objects.import_from_saltedge(
        account_foo_external.user,
        account_foo_external.connection.external_id,
        account_foo_external.external_id,
        transactions_api,
    )

    for imported, mock in zip(imported_transactions, mock_transactions):
        escaped_category = mock.category.replace("_", " ")
        assert (
            imported.category
            == Category.objects.filter(
                name__iexact=escaped_category, user=account_foo_external.user
            )[0]
        )


def test_transaction_import_from_saltedge_uncategorized_category(
    account_foo_external, transactions_api, saltedge_transaction_factory
):
    mock_transactions = [
        saltedge_transaction_factory(
            id="1", category="xyz", account_id=account_foo_external.external_id,
        ),
    ]
    transactions_api.transactions_get.return_value = saltedge_client.TransactionsResponse(
        data=mock_transactions
    )

    imported_transactions = Transaction.objects.import_from_saltedge(
        account_foo_external.user,
        account_foo_external.connection.external_id,
        account_foo_external.external_id,
        transactions_api,
    )

    uncategorized = Category.objects.get(
        name="Uncategorized", user=account_foo_external.user
    )
    for imported, mock in zip(imported_transactions, mock_transactions):
        assert imported.category == uncategorized


def test_transaction_get_balance_filter_by_user(
    user_factory, account_factory, category_factory, transaction_factory
):
    user_abc = user_factory("abc")
    user_xyz = user_factory("xyz")

    account_abc = account_factory("abc", user=user_abc)
    account_xyz = account_factory("xyz", user=user_xyz)

    category_abc = category_factory("abc", user_abc)
    category_xyz = category_factory("xyz", user_xyz)

    transaction_abc = transaction_factory(
        amount=123.00, account=account_abc, user=user_abc, category=category_abc
    )
    transaction_xyz = transaction_factory(
        amount=256.00, account=account_xyz, user=user_xyz, category=category_xyz
    )

    output = Transaction.objects.get_balance(
        accounts=[account_abc, account_xyz], user=user_abc,
    )

    assert output == {"abc": 123.00, "Total": 123.00}


def test_transaction_get_balance_filter_by_account(
    user_factory, account_factory, category_factory, transaction_factory
):
    user_abc = user_factory("abc")

    account_abc_1 = account_factory("abc_1", user=user_abc)
    account_abc_2 = account_factory("abc_2", user=user_abc)
    account_abc_3 = account_factory("abc_3", user=user_abc)

    category_abc = category_factory("abc", user_abc)

    transaction_abc_1 = transaction_factory(
        amount=4.00, account=account_abc_1, user=user_abc, category=category_abc
    )
    transaction_abc_2 = transaction_factory(
        amount=5.00, account=account_abc_2, user=user_abc, category=category_abc
    )
    transaction_abc_3 = transaction_factory(
        amount=6.00, account=account_abc_3, user=user_abc, category=category_abc
    )

    output = Transaction.objects.get_balance(
        accounts=[account_abc_1, account_abc_2], user=user_abc,
    )

    assert output == {"abc": 4.00 + 5.00, "Total": 4.00 + 5.00}


def test_transaction_get_balance_per_category(
    user_factory, account_factory, category_factory, transaction_factory
):
    user_abc = user_factory("abc")
    account_abc = account_factory("abc", user=user_abc)
    category_abc_1 = category_factory("abc_1", user_abc)
    category_abc_2 = category_factory("abc_2", user_abc)

    transaction_abc_1 = transaction_factory(
        amount=4.00, account=account_abc, user=user_abc, category=category_abc_1
    )
    transaction_abc_2 = transaction_factory(
        amount=5.00, account=account_abc, user=user_abc, category=category_abc_2
    )

    output = Transaction.objects.get_balance(accounts=[account_abc], user=user_abc,)

    assert output == {"abc_1": 4.00, "abc_2": 5.00, "Total": 4.00 + 5.00}


def test_transaction_get_balance_filter_by_from_date(
    user_factory, account_factory, category_factory, transaction_factory
):
    user_abc = user_factory("abc")
    account_abc = account_factory("abc", user=user_abc)
    category_abc = category_factory("abc", user_abc)

    transaction_abc_1 = transaction_factory(
        amount=4.00,
        account=account_abc,
        date=datetime.date(2020, 2, 1),
        user=user_abc,
        category=category_abc,
    )
    transaction_abc_2 = transaction_factory(
        amount=5.00,
        account=account_abc,
        date=datetime.date(2020, 3, 1),
        user=user_abc,
        category=category_abc,
    )
    transaction_abc_3 = transaction_factory(
        amount=6.00,
        account=account_abc,
        date=datetime.date(2020, 4, 1),
        user=user_abc,
        category=category_abc,
    )

    output = Transaction.objects.get_balance(
        accounts=[account_abc], user=user_abc, from_date=datetime.date(2020, 3, 1)
    )

    assert output == {"abc": 5.00 + 6.00, "Total": 5.00 + 6.00}


def test_transaction_get_balance_filter_by_to_date(
    user_factory, account_factory, category_factory, transaction_factory
):
    user_abc = user_factory("abc")
    account_abc = account_factory("abc", user=user_abc)
    category_abc = category_factory("abc", user_abc)

    transaction_abc_1 = transaction_factory(
        amount=4.00,
        account=account_abc,
        date=datetime.date(2020, 2, 1),
        user=user_abc,
        category=category_abc,
    )
    transaction_abc_2 = transaction_factory(
        amount=5.00,
        account=account_abc,
        date=datetime.date(2020, 3, 1),
        user=user_abc,
        category=category_abc,
    )
    transaction_abc_3 = transaction_factory(
        amount=6.00,
        account=account_abc,
        date=datetime.date(2020, 4, 1),
        user=user_abc,
        category=category_abc,
    )

    output = Transaction.objects.get_balance(
        accounts=[account_abc], user=user_abc, to_date=datetime.date(2020, 3, 1)
    )

    assert output == {"abc": 4.00 + 5.00, "Total": 4.00 + 5.00}
