from typing import Dict

from budget.forms import (
    CreateConnectionForm,
    ImportAccountsForm,
    ImportConnectionsForm,
    ImportTransactionsForm,
    ReportBalanceForm,
)
from budget.models import Account, Connection
from users.models import User


def test_import_accounts_form_valid(user_foo: User, connection_foo: Connection) -> None:
    data = {
        "connection": connection_foo,
    }
    form = ImportAccountsForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_import_accounts_form_empty_connection(user_foo: User) -> None:
    form = ImportAccountsForm(data={}, user=user_foo)
    form.is_valid()
    assert "connection" in form.errors


def test_import_transactions_form_valid(
    user_foo: User, account_foo_external: Account
) -> None:
    data = {
        "account": account_foo_external,
    }
    form = ImportTransactionsForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_import_transactions_form_empty_account(user_foo: User) -> None:
    form = ImportTransactionsForm(data={}, user=user_foo)
    form.is_valid()
    assert "account" in form.errors


def test_import_transactions_form_internal_account(
    user_foo: User, account_foo: Account
) -> None:
    data = {
        "account": account_foo,
    }
    form = ImportTransactionsForm(data=data, user=user_foo)
    form.is_valid()
    assert "account" in form.errors


def test_create_connection_form_valid() -> None:
    form = CreateConnectionForm(data={})
    assert form.is_valid() is True


def test_import_connections_form_valid() -> None:
    form = ImportConnectionsForm(data={})
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
