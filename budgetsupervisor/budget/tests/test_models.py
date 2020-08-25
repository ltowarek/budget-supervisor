from budget.models import Connection, Account, Category, Transaction
import pytest
import datetime


@pytest.fixture
def user_factory(db, django_user_model):
    def create_user(
        username,
        password="password",
        first_name="foo",
        last_name="bar",
        email="foo@bar.com",
        is_staff=False,
        is_superuser=False,
        is_active=True,
    ):
        return django_user_model.objects.create(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
        )

    return create_user


@pytest.fixture
def user_foo(user_factory):
    return user_factory(username="foo")


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


def test_connection_str(connection_foo):
    assert str(connection_foo) == "foo"


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


def test_account_str(account_foo):
    assert str(account_foo) == "foo"


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


def test_transaction_str(transaction_foo):
    assert str(transaction_foo) == "1"


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
