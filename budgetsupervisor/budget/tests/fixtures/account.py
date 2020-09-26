import pytest
from budget.models import Account


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
