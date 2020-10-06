from budget.forms import (
    CreateConnectionForm,
    ImportAccountsForm,
    ImportConnectionsForm,
    ImportTransactionsForm,
    ReportBalanceForm,
)


def test_import_accounts_form_valid(user_foo, connection_foo_external):
    data = {
        "connection": connection_foo_external,
    }
    form = ImportAccountsForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_import_accounts_form_empty_connection(user_foo):
    data = {}
    form = ImportAccountsForm(data=data, user=user_foo)
    form.is_valid()
    assert "connection" in form.errors


def test_import_transactions_form_valid(user_foo, account_foo_external):
    data = {
        "account": account_foo_external,
    }
    form = ImportTransactionsForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_import_transactions_form_empty_account(user_foo):
    data = {}
    form = ImportTransactionsForm(data=data, user=user_foo)
    form.is_valid()
    assert "account" in form.errors


def test_import_transactions_form_internal_account(user_foo, account_foo):
    data = {
        "account": account_foo,
    }
    form = ImportTransactionsForm(data=data, user=user_foo)
    form.is_valid()
    assert "account" in form.errors


def test_create_connection_form_valid():
    data = {}
    form = CreateConnectionForm(data=data)
    assert form.is_valid() is True


def test_import_connections_form_valid():
    data = {}
    form = ImportConnectionsForm(data=data)
    assert form.is_valid() is True


def test_report_balance_form_valid_single_account(user_foo, account_foo):
    data = {"accounts": [account_foo]}
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_valid_multiple_accounts(user_foo, account_factory):
    account_a = account_factory("a")
    account_b = account_factory("b")
    data = {"accounts": [account_a, account_b]}
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_valid_with_from_date(user_foo, account_foo):
    data = {"accounts": [account_foo], "from_date": "2020-05-03"}
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_valid_with_to_date(user_foo, account_foo):
    data = {"accounts": [account_foo], "to_date": "2020-05-03"}
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_valid_with_from_and_to_date(user_foo, account_foo):
    data = {
        "accounts": [account_foo],
        "from_date": "2020-05-03",
        "to_date": "2020-06-03",
    }
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_empty_accounts(user_foo):
    data = {
        "accounts": [],
    }
    form = ReportBalanceForm(data=data, user=user_foo)
    form.is_valid()
    assert "accounts" in form.errors


def test_report_balance_form_to_date_before_from_date(user_foo, account_foo):
    data = {
        "accounts": [account_foo],
        "from_date": "2020-05-03",
        "to_date": "2020-04-03",
    }
    form = ReportBalanceForm(data=data, user=user_foo)
    form.is_valid()
    assert "to_date" in form.errors
