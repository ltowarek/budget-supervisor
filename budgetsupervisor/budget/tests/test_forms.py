import datetime
from typing import Any, Callable, Dict

import pytest
import swagger_client as saltedge_client
from budget.forms import (
    CreateConnectionForm,
    CreateTransactionForm,
    RefreshConnectionForm,
    ReportBalanceForm,
    ReportCategoryBalanceForm,
    ReportIncomeForm,
    UpdateAccountForm,
    UpdateTransactionForm,
)
from budget.models import Account, Category, Transaction
from budget.services import create_initial_balance
from users.models import User


def test_create_connection_form_default() -> None:
    form = CreateConnectionForm(data={})
    assert form.is_valid() is True


def test_create_connection_form_from_date_valid() -> None:
    data = {
        "from_date": datetime.date.today(),
    }
    form = CreateConnectionForm(data=data)
    assert form.is_valid() is True


def test_create_connection_form_from_date_365_days_ago() -> None:
    data = {
        "from_date": datetime.date.today() - datetime.timedelta(days=365),
    }
    form = CreateConnectionForm(data=data)
    assert form.is_valid() is True


def test_create_connection_form_from_date_366_days_ago() -> None:
    data = {
        "from_date": datetime.date.today() - datetime.timedelta(days=366),
    }
    form = CreateConnectionForm(data=data)
    form.is_valid()
    assert "from_date" in form.errors


def test_create_connection_form_from_date_in_future() -> None:
    data = {
        "from_date": datetime.date.today() + datetime.timedelta(days=1),
    }
    form = CreateConnectionForm(data=data)
    form.is_valid()
    assert "from_date" in form.errors


def test_create_connection_form_to_date_valid() -> None:
    data = {
        "to_date": datetime.date.today(),
    }
    form = CreateConnectionForm(data=data)
    assert form.is_valid() is True


def test_create_connection_form_to_date_in_past() -> None:
    data = {
        "to_date": datetime.date.today() - datetime.timedelta(days=1),
    }
    form = CreateConnectionForm(data=data)
    form.is_valid()
    assert "to_date" in form.errors


def test_create_connection_form_to_date_before_from_date() -> None:
    data = {
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today() - datetime.timedelta(days=1),
    }
    form = CreateConnectionForm(data=data)
    form.is_valid()
    assert "to_date" in form.errors


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


def test_create_transaction_accounts_are_ordered(
    user_foo: User, account_factory: Callable[..., Account],
) -> None:
    account_c = account_factory(name="f", alias="c")
    account_b = account_factory(name="e", alias="b")
    account_d = account_factory(name="d")
    account_a = account_factory(name="a")
    form = CreateTransactionForm(user=user_foo)
    assert list(form.fields["account"].queryset) == [
        account_a,
        account_b,
        account_c,
        account_d,
    ]


def test_create_transaction_categories_are_ordered(
    user_foo: User, category_factory: Callable[..., Category],
) -> None:
    category_c = category_factory(name="c")
    category_b = category_factory(name="b")
    category_a = category_factory(name="a")
    form = CreateTransactionForm(user=user_foo)
    assert list(form.fields["category"].queryset) == [
        category_a,
        category_b,
        category_c,
    ]


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


def test_update_transaction_amount_field_enabled(transaction_foo: Transaction) -> None:
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


def test_update_transaction_account_field_enabled(transaction_foo: Transaction) -> None:
    form = UpdateTransactionForm(data={}, instance=transaction_foo)
    assert form.fields["account"].disabled is False


def test_update_transaction_account_field_disabled(
    transaction_foo_external: Transaction,
) -> None:
    form = UpdateTransactionForm(data={}, instance=transaction_foo_external)
    assert form.fields["account"].disabled is True


def test_update_transaction_accounts_are_ordered(
    transaction_foo: Transaction, account_factory: Callable[..., Account]
) -> None:
    account_c = account_factory(name="f", alias="c", user=transaction_foo.user)
    account_b = account_factory(name="e", alias="b", user=transaction_foo.user)
    account_d = account_factory(name="d", user=transaction_foo.user)
    account_a = account_factory(name="a", user=transaction_foo.user)
    form = UpdateTransactionForm(instance=transaction_foo)
    assert list(form.fields["account"].queryset) == [
        account_a,
        account_b,
        account_c,
        account_d,
        transaction_foo.account,
    ]


def test_update_transaction_categories_are_ordered(
    transaction_foo: Transaction, category_factory: Callable[..., Category]
) -> None:
    category_c = category_factory(name="c", user=transaction_foo.user)
    category_b = category_factory(name="b", user=transaction_foo.user)
    category_a = category_factory(name="a", user=transaction_foo.user)
    form = UpdateTransactionForm(instance=transaction_foo)
    assert list(form.fields["category"].queryset) == [
        category_a,
        category_b,
        category_c,
    ]


def test_update_transaction_other_users_accounts_are_not_visible(
    user_factory: Callable[..., User],
    account_factory: Callable[..., Account],
    transaction_factory: Callable[..., Transaction],
) -> None:
    user_a = user_factory(username="a")
    account_a = account_factory(name="a", user=user_a)
    user_b = user_factory(username="b")
    _ = account_factory(name="b", user=user_b)
    transaction = transaction_factory(account=account_a, user=user_a)
    form = UpdateTransactionForm(instance=transaction)
    assert list(form.fields["account"].queryset) == [account_a]


def test_update_transaction_other_users_categories_are_not_visible(
    user_factory: Callable[..., User],
    category_factory: Callable[..., Category],
    transaction_factory: Callable[..., Transaction],
) -> None:
    user_a = user_factory(username="a")
    category_a = category_factory(name="a", user=user_a)
    user_b = user_factory(username="b")
    _ = category_factory(name="b", user=user_b)
    transaction = transaction_factory(category=category_a, user=user_a)
    form = UpdateTransactionForm(instance=transaction)
    assert list(form.fields["category"].queryset) == [category_a]


def test_refresh_connection_form_valid() -> None:
    form = RefreshConnectionForm(data={})
    assert form.is_valid() is True


def test_report_income_form_valid_single_account(
    user_foo: User, account_foo: Account
) -> None:
    data = {
        "accounts": [account_foo],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportIncomeForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_income_form_valid_multiple_accounts(
    user_foo: User, account_factory: Account
) -> None:
    account_a = account_factory("a")
    account_b = account_factory("b")
    data = {
        "accounts": [account_a, account_b],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportIncomeForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_income_form_valid_with_from_and_to_date(
    user_foo: User, account_foo: Account
) -> None:
    data = {
        "accounts": [account_foo],
        "from_date": "2020-05-03",
        "to_date": "2020-06-03",
    }
    form = ReportIncomeForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_income_form_empty_accounts(user_foo: User) -> None:
    data: Dict = {
        "accounts": [],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportIncomeForm(data=data, user=user_foo)
    form.is_valid()
    assert "accounts" in form.errors


def test_report_income_form_to_date_before_from_date(
    user_foo: User, account_foo: Account
) -> None:
    data = {
        "accounts": [account_foo],
        "from_date": "2020-05-03",
        "to_date": "2020-04-03",
    }
    form = ReportIncomeForm(data=data, user=user_foo)
    form.is_valid()
    assert "to_date" in form.errors


def test_report_income_form_with_excluded_category(
    user_foo: User, account_foo: Account, category_foo: Category
) -> None:
    data = {
        "accounts": [account_foo],
        "excluded_categories": [category_foo],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportIncomeForm(data=data, user=user_foo)
    assert form.is_valid()


def test_report_income_form_with_excluded_categories(
    user_foo: User, account_foo: Account, category_factory: Callable[..., Category]
) -> None:
    categories = [
        category_factory(name="a", user=account_foo.user),
        category_factory(name="b", user=account_foo.user),
    ]
    data: Dict[str, Any] = {
        "accounts": [account_foo],
        "excluded_categories": categories,
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportIncomeForm(data=data, user=user_foo)
    assert form.is_valid()


def test_report_income_form_with_unknown_excluded_category(
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
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportIncomeForm(data=data, user=user_foo)
    form.is_valid()
    assert "excluded_categories" in form.errors


def test_report_income_form_accounts_are_ordered(
    user_foo: User,
    account_factory: Callable[..., Account],
    user_factory: Callable[..., User],
) -> None:
    account_c = account_factory(name="f", alias="c")
    account_b = account_factory(name="e", alias="b")
    account_d = account_factory(name="d")
    account_a = account_factory(name="a")
    form = ReportIncomeForm(user=user_foo)
    assert list(form.fields["accounts"].queryset) == [
        account_a,
        account_b,
        account_c,
        account_d,
    ]


def test_report_income_form_excluded_categories_are_ordered(
    user_foo: User,
    category_factory: Callable[..., Category],
    user_factory: Callable[..., User],
) -> None:
    category_c = category_factory(name="c")
    category_b = category_factory(name="b")
    category_a = category_factory(name="a")
    form = ReportIncomeForm(user=user_foo)
    assert list(form.fields["excluded_categories"].queryset) == [
        category_a,
        category_b,
        category_c,
    ]


def test_report_balance_form_valid_single_account(
    user_foo: User, account_foo: Account
) -> None:
    data = {
        "accounts": [account_foo],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_balance_form_valid_multiple_accounts(
    user_foo: User, account_factory: Account
) -> None:
    account_a = account_factory("a")
    account_b = account_factory("b")
    data = {
        "accounts": [account_a, account_b],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
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
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
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


def test_report_balance_form_accounts_are_ordered(
    user_foo: User,
    account_factory: Callable[..., Account],
    user_factory: Callable[..., User],
) -> None:
    account_c = account_factory(name="f", alias="c")
    account_b = account_factory(name="e", alias="b")
    account_d = account_factory(name="d")
    account_a = account_factory(name="a")
    form = ReportBalanceForm(user=user_foo)
    assert list(form.fields["accounts"].queryset) == [
        account_a,
        account_b,
        account_c,
        account_d,
    ]


def test_report_category_balance_form_valid_single_category(
    user_foo: User, category_foo: Category, account_foo: Account
) -> None:
    data = {
        "categories": [category_foo],
        "accounts": [account_foo],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportCategoryBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_category_balance_form_valid_multiple_categories(
    user_foo: User, category_factory: Callable[..., Category], account_foo: Account
) -> None:
    category_a = category_factory("a")
    category_b = category_factory("b")
    data = {
        "categories": [category_a, category_b],
        "accounts": [account_foo],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportCategoryBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_category_balance_form_valid_single_account(
    user_foo: User, category_foo: Category, account_foo: Account
) -> None:
    data = {
        "categories": [category_foo],
        "accounts": [account_foo],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportCategoryBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_category_balance_form_valid_multiple_accounts(
    user_foo: User, category_foo: Category, account_factory: Callable[..., Account]
) -> None:
    account_a = account_factory("a")
    account_b = account_factory("b")
    data = {
        "categories": [category_foo],
        "accounts": [account_a, account_b],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportCategoryBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_category_balance_form_valid_with_from_and_to_date(
    user_foo: User, category_foo: Category, account_foo: Account
) -> None:
    data = {
        "categories": [category_foo],
        "accounts": [account_foo],
        "from_date": "2020-05-03",
        "to_date": "2020-06-03",
    }
    form = ReportCategoryBalanceForm(data=data, user=user_foo)
    assert form.is_valid() is True


def test_report_category_balance_form_empty_categories(
    user_foo: User, account_foo: Account
) -> None:
    data: Dict = {
        "categories": [],
        "accounts": [account_foo],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportCategoryBalanceForm(data=data, user=user_foo)
    form.is_valid()
    assert "categories" in form.errors


def test_report_category_balance_form_empty_accounts(
    user_foo: User, category_foo: Category
) -> None:
    data: Dict = {
        "categories": [category_foo],
        "accounts": [],
        "from_date": datetime.date.today(),
        "to_date": datetime.date.today(),
    }
    form = ReportCategoryBalanceForm(data=data, user=user_foo)
    form.is_valid()
    assert "accounts" in form.errors


def test_report_category_balance_form_to_date_before_from_date(
    user_foo: User, category_foo: Category, account_foo: Account
) -> None:
    data = {
        "categories": [category_foo],
        "accounts": [account_foo],
        "from_date": "2020-05-03",
        "to_date": "2020-04-03",
    }
    form = ReportCategoryBalanceForm(data=data, user=user_foo)
    form.is_valid()
    assert "to_date" in form.errors


def test_report_category_balance_form_accounts_are_ordered(
    user_foo: User,
    account_factory: Callable[..., Account],
    user_factory: Callable[..., User],
) -> None:
    account_c = account_factory(name="f", alias="c")
    account_b = account_factory(name="e", alias="b")
    account_d = account_factory(name="d")
    account_a = account_factory(name="a")
    form = ReportCategoryBalanceForm(user=user_foo)
    assert list(form.fields["accounts"].queryset) == [
        account_a,
        account_b,
        account_c,
        account_d,
    ]


def test_report_category_balance_form_categories_are_ordered(
    user_foo: User,
    category_factory: Callable[..., Category],
    user_factory: Callable[..., User],
) -> None:
    category_c = category_factory(name="c")
    category_b = category_factory(name="b")
    category_a = category_factory(name="a")
    form = ReportCategoryBalanceForm(user=user_foo)
    assert list(form.fields["categories"].queryset) == [
        category_a,
        category_b,
        category_c,
    ]
