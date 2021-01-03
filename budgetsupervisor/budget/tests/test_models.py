from typing import Callable

from budget.models import Account, Category, Connection, Transaction
from users.models import User


def test_connection_str(connection_foo: Connection) -> None:
    assert str(connection_foo) == "foo"


def test_account_str(account_foo: Account) -> None:
    assert str(account_foo) == "foo"


def test_category_str(category_foo: Category) -> None:
    assert str(category_foo) == "foo"


def test_transaction_str(transaction_foo: Transaction) -> None:
    assert str(transaction_foo) == "transaction foo"


def test_delete_transaction_when_account_is_deleted(
    transaction_foo_external: Transaction, account_foo_external: Account
) -> None:
    account_foo_external.delete()
    assert not Transaction.objects.filter(pk=transaction_foo_external.pk).exists()


def test_do_not_delete_account_when_connection_is_deleted(
    account_foo_external: Account, connection_foo: Connection
) -> None:
    connection_foo.delete()
    account_foo_external.refresh_from_db()
    assert Account.objects.filter(pk=account_foo_external.pk).exists()
    assert account_foo_external.connection is None


def test_delete_transaction_when_user_is_deleted(
    transaction_foo: Transaction, user_foo: User
) -> None:
    user_foo.delete()
    assert not Transaction.objects.filter(pk=transaction_foo.pk).exists()


def test_delete_account_when_user_is_deleted(
    account_foo: Account, user_foo: User
) -> None:
    user_foo.delete()
    assert not Account.objects.filter(pk=account_foo.pk).exists()


def test_delete_connection_when_user_is_deleted(
    connection_foo: Connection, user_foo: User
) -> None:
    user_foo.delete()
    assert not Connection.objects.filter(pk=connection_foo.pk).exists()


def test_transaction_category_is_set_to_null_when_category_is_deleted(
    transaction_factory: Callable[..., Transaction], category_foo: Category
) -> None:
    transaction = transaction_factory(category=category_foo)
    category_foo.delete()
    transaction.refresh_from_db()
    assert transaction.category is None
