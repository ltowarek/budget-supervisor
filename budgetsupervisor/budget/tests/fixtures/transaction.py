import pytest
import datetime
from budget.models import Transaction


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
