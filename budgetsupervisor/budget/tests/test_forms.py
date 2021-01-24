from typing import Any, Callable, Dict

import pytest
import swagger_client as saltedge_client
from budget.forms import (
    CreateConnectionForm,
    RefreshConnectionForm,
    ReportBalanceForm,
    UpdateAccountForm,
    UpdateTransactionForm,
)
from budget.models import Account, Category, Transaction
from budget.services import create_initial_balance
from users.models import User


def test_create_connection_form_valid() -> None:
    form = CreateConnectionForm(data={})
    assert form.is_valid() is True


def test_update_account_form_valid(account_foo: Account) -> None:
    form = UpdateAccountForm(
        data={
            "name": "xyz",
            "alias": "abc",
            "account_type": Account.AccountType.ACCOUNT,
        },
        instance=account_foo,
    )
    assert form.is_valid() is True


def test_update_account_name_field_enabled(account_foo: Account) -> None:
    form = UpdateAccountForm(data={}, instance=account_foo)
    assert form.fields["name"].disabled is False


def test_update_account_name_field_disabled(account_foo_external: Account) -> None:
    form = UpdateAccountForm(data={}, instance=account_foo_external)
    assert form.fields["name"].disabled is True


def test_update_account_account_type_field_enabled(account_foo: Account) -> None:
    form = UpdateAccountForm(data={}, instance=account_foo)
    assert form.fields["account_type"].disabled is False


def test_update_account_account_type_field_disabled(
    account_foo_external: Account,
) -> None:
    form = UpdateAccountForm(data={}, instance=account_foo_external)
    assert form.fields["account_type"].disabled is True


def test_update_account_alias_field_disabled(account_foo_external: Account,) -> None:
    form = UpdateAccountForm(data={}, instance=account_foo_external)
    assert form.fields["alias"].disabled is True


def test_update_transaction_form_valid(transaction_foo: Transaction) -> None:
    form = UpdateTransactionForm(
        data={
            "date": transaction_foo.date,
            "amount": transaction_foo.amount,
            "payee": transaction_foo.payee,
            "category": transaction_foo.category,
            "description": transaction_foo.description,
            "account": transaction_foo.account,
        },
        instance=transaction_foo,
    )
    assert form.is_valid() is True


def test_update_transaction_date_field_enabled(transaction_foo: Transaction) -> None:
    form = UpdateTransactionForm(data={}, instance=transaction_foo)
    assert form.fields["date"].disabled is False


def test_update_transaction_date_field_disabled(
    transaction_foo_external: Transaction,
) -> None:
    form = UpdateTransactionForm(data={}, instance=transaction_foo_external)
    assert form.fields["date"].disabled is True


def test_update_transaction_amount_field_enabled(transaction_foo: Transaction,) -> None:
    form = UpdateTransactionForm(data={}, instance=transaction_foo)
    assert form.fields["amount"].disabled is False


def test_update_transaction_amount_field_disabled(
    transaction_foo_external: Transaction,
) -> None:
    form = UpdateTransactionForm(data={}, instance=transaction_foo_external)
    assert form.fields["amount"].disabled is True


def test_update_transaction_description_field_enabled(
    transaction_foo: Transaction,
) -> None:
    form = UpdateTransactionForm(data={}, instance=transaction_foo)
    assert form.fields["description"].disabled is False


def test_update_transaction_description_field_disabled(
    transaction_foo_external: Transaction,
) -> None:
    form = UpdateTransactionForm(data={}, instance=transaction_foo_external)
    assert form.fields["description"].disabled is True


@pytest.fixture
def initial_transaction(
    account_foo_external: Account,
    saltedge_account: saltedge_client.Account,
    saltedge_transaction: saltedge_client.Transaction,
) -> Transaction:
    return create_initial_balance(
        account_foo_external, saltedge_account, [saltedge_transaction]
    )


def test_update_transaction_initial_transaction_date_field_enabled(
    initial_transaction: Transaction,
) -> None:
    form = UpdateTransactionForm(data={}, instance=initial_transaction)
    assert form.fields["date"].disabled is False


def test_update_transaction_initial_transaction_amount_field_enabled(
    initial_transaction: Transaction,
) -> None:
    form = UpdateTransactionForm(data={}, instance=initial_transaction)
    assert form.fields["amount"].disabled is False


def test_update_transaction_initial_transaction_description_field_enabled(
    initial_transaction: Transaction,
) -> None:
    form = UpdateTransactionForm(data={}, instance=initial_transaction)
    assert form.fields["description"].disabled is False


def test_update_transaction_account_field_enabled(
    transaction_foo: Transaction,
) -> None:
    form = UpdateTransactionForm(data={}, instance=transaction_foo)
    assert form.fields["account"].disabled is False


def test_update_transaction_account_field_disabled(
    transaction_foo_external: Transaction,
) -> None:
    form = UpdateTransactionForm(data={}, instance=transaction_foo_external)
    assert form.fields["account"].disabled is True


def test_refresh_connection_form_valid() -> None:
    form = RefreshConnectionForm(data={})
    assert form.is_valid() is True


def test_report_balance_form_valid_single_account(
    user_foo: User, account_foo: Account
) -> None:
    data = {"accounts": [account_foo]}
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_valid_multiple_accounts(
    user_foo: User, account_factory: Account
) -> None:
    account_a = account_factory("a")
    account_b = account_factory("b")
    data = {"accounts": [account_a, account_b]}
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_valid_with_from_date(
    user_foo: User, account_foo: Account
) -> None:
    data = {"accounts": [account_foo], "from_date": "2020-05-03"}
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_valid_with_to_date(
    user_foo: User, account_foo: Account
) -> None:
    data = {"accounts": [account_foo], "to_date": "2020-05-03"}
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_valid_with_from_and_to_date(
    user_foo: User, account_foo: Account
) -> None:
    data = {
        "accounts": [account_foo],
        "from_date": "2020-05-03",
        "to_date": "2020-06-03",
    }
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_empty_accounts(user_foo: User) -> None:
    data: Dict = {
        "accounts": [],
    }
    form = ReportBalanceForm(data=data, user=user_foo)
    form.is_valid()
    assert "accounts" in form.errors


def test_report_balance_form_to_date_before_from_date(
    user_foo: User, account_foo: Account
) -> None:
    data = {
        "accounts": [account_foo],
        "from_date": "2020-05-03",
        "to_date": "2020-04-03",
    }
    form = ReportBalanceForm(data=data, user=user_foo)
    form.is_valid()
    assert "to_date" in form.errors


def test_report_balance_form_with_excluded_category(
    user_foo: User, account_foo: Account, category_foo: Category
) -> None:
    data = {
        "accounts": [account_foo],
        "excluded_categories": [category_foo],
    }
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid()


def test_report_balance_form_with_excluded_categories(
    user_foo: User, account_foo: Account, category_factory: Callable[..., Category]
) -> None:
    categories = [
        category_factory(name="a", user=account_foo.user),
        category_factory(name="b", user=account_foo.user),
    ]
    data: Dict[str, Any] = {
        "accounts": [account_foo],
        "excluded_categories": categories,
    }
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid()


def test_report_balance_form_with_unknown_excluded_category(
    user_foo: User,
    account_foo: Account,
    category_factory: Callable[..., Category],
    user_factory: Callable[..., User],
) -> None:
    categories = [
        category_factory(name="a", user=user_factory(username="bar")),
    ]
    data: Dict[str, Any] = {
        "accounts": [account_foo],
        "excluded_categories": categories,
    }
    form = ReportBalanceForm(data=data, user=user_foo)
    form.is_valid()
    assert "excluded_categories" in form.errors
