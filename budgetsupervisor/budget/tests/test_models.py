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
