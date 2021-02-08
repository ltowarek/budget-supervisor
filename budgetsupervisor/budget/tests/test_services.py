import datetime
from decimal import Decimal
from typing import Any, Callable, Dict, List

import pytest
import swagger_client as saltedge_client
from budget.models import Account, Category, Connection, Transaction
from budget.services import (
    add_month,
    create_initial_balance,
    diff_month,
    filter_transactions,
    get_balance_record,
    get_balance_record_per_month,
    get_balance_records_summary,
    get_balance_report,
    get_category_balance,
    get_category_balance_record_per_month,
    get_category_balance_records_summary,
    get_category_balance_report,
    get_category_balance_report_header,
    get_date_range_per_month,
    get_ending_balance,
    get_expenses,
    get_income_record,
    get_income_record_per_month,
    get_income_records_summary,
    get_income_report,
    get_income_transactions,
    get_month_end,
    get_month_start,
    get_opening_balance,
    get_revenue,
    import_saltedge_accounts,
    import_saltedge_connection,
    import_saltedge_connections,
    import_saltedge_transactions,
    query_dict_to_transaction_filter_query,
    transaction_filter_query_to_query_dict,
)
from django.http.request import QueryDict
from pytest_mock import MockFixture
from users.models import User


class TestImportSaltedgeConnection:
    def test_connection_is_created(
        self, saltedge_connection: saltedge_client.Connection, user_foo: User
    ) -> None:
        new_connection, is_created = import_saltedge_connection(
            saltedge_connection, user_foo
        )
        assert new_connection.provider == saltedge_connection.provider_name
        assert new_connection.user == user_foo
        assert new_connection.external_id == int(saltedge_connection.id)
        assert is_created is True

    def test_connection_is_updated(
        self,
        connection_foo: Connection,
        saltedge_connection: saltedge_client.Connection,
        user_foo: User,
    ) -> None:
        connection_foo.external_id = int(saltedge_connection.id)
        connection_foo.save()
        updated_connection, is_created = import_saltedge_connection(
            saltedge_connection, user_foo
        )
        assert updated_connection.id == connection_foo.id
        assert updated_connection.provider == saltedge_connection.provider_name
        assert updated_connection.user == user_foo
        assert updated_connection.external_id == int(saltedge_connection.id)
        assert is_created is False


class TestImportSaltedgeConnections:
    @pytest.fixture
    def saltedge_connections(
        self, saltedge_connection_factory: Callable[..., saltedge_client.Connection]
    ) -> List[saltedge_client.Connection]:
        return [
            saltedge_connection_factory(id="1", provider_name="a"),
            saltedge_connection_factory(id="2", provider_name="b"),
            saltedge_connection_factory(id="3", provider_name="c"),
        ]

    @pytest.fixture
    def connections(
        self,
        connection_factory: Callable[..., Connection],
        saltedge_connections: List[saltedge_client.Connection],
    ) -> List[Connection]:
        connections = []
        for saltedge_connection in saltedge_connections:
            connections.append(
                connection_factory(
                    provider=saltedge_connection.provider_name + "_tmp",
                    external_id=int(saltedge_connection.id),
                )
            )
        return connections

    def test_connections_are_created(
        self, saltedge_connections: List[saltedge_client.Connection], user_foo: User
    ) -> None:
        output_tuples = import_saltedge_connections(saltedge_connections, user_foo)
        for output_tuple, saltedge_connection in zip(
            output_tuples, saltedge_connections
        ):
            new_connection, is_created = output_tuple
            assert new_connection.provider == saltedge_connection.provider_name
            assert new_connection.user == user_foo
            assert new_connection.external_id == int(saltedge_connection.id)
            assert is_created is True

    def test_connections_are_updated(
        self,
        connections: List[Connection],
        saltedge_connections: List[saltedge_client.Connection],
        user_foo: User,
    ) -> None:
        output_tuples = import_saltedge_connections(saltedge_connections, user_foo)
        for output_tuple, saltedge_connection in zip(
            output_tuples, saltedge_connections
        ):
            updated_connection, is_created = output_tuple
            assert updated_connection.provider == saltedge_connection.provider_name
            assert updated_connection.user == user_foo
            assert updated_connection.external_id == int(saltedge_connection.id)
            assert is_created is False


class TestImportSaltedgeAccounts:
    @pytest.fixture
    def saltedge_accounts(
        self,
        saltedge_account_factory: Callable[..., saltedge_client.Account],
        connection_foo: Connection,
    ) -> List[saltedge_client.Account]:
        return [
            saltedge_account_factory(
                id="1", name="a", connection_id=connection_foo.external_id
            ),
            saltedge_account_factory(
                id="2", name="b", connection_id=connection_foo.external_id
            ),
            saltedge_account_factory(
                id="3", name="c", connection_id=connection_foo.external_id
            ),
        ]

    @pytest.fixture
    def accounts(
        self,
        account_factory: Callable[..., Account],
        saltedge_accounts: List[saltedge_client.Account],
    ) -> List[Account]:
        accounts = []
        for saltedge_account in saltedge_accounts:
            accounts.append(
                account_factory(
                    name=saltedge_account.name + "_tmp",
                    external_id=int(saltedge_account.id),
                )
            )
        return accounts

    def test_accounts_are_created(
        self,
        saltedge_accounts: List[saltedge_client.Account],
        user_foo: User,
        connection_foo: Connection,
    ) -> None:
        output_tuples = import_saltedge_accounts(saltedge_accounts, user_foo)
        for output_tuple, saltedge_account in zip(output_tuples, saltedge_accounts):
            new_account, is_created = output_tuple
            assert new_account.name == saltedge_account.name
            assert new_account.alias == ""
            assert new_account.user == user_foo
            assert new_account.external_id == int(saltedge_account.id)
            assert new_account.connection == connection_foo
            assert is_created is True

    def test_accounts_are_updated(
        self,
        accounts: List[Account],
        saltedge_accounts: List[saltedge_client.Account],
        user_foo: User,
        connection_foo: Connection,
    ) -> None:
        output_tuples = import_saltedge_accounts(saltedge_accounts, user_foo)
        for output_tuple, saltedge_account in zip(output_tuples, saltedge_accounts):
            updated_account, is_created = output_tuple
            assert updated_account.name == saltedge_account.name
            assert updated_account.alias == ""
            assert updated_account.user == user_foo
            assert updated_account.external_id == int(saltedge_account.id)
            assert updated_account.connection == connection_foo
            assert is_created is False

    def test_account_type_is_not_overriden(
        self,
        accounts: List[Account],
        saltedge_accounts: List[saltedge_client.Account],
        user_foo: User,
    ) -> None:
        original_account_types = [a.account_type for a in accounts]
        output_tuples = import_saltedge_accounts(saltedge_accounts, user_foo)
        for output_tuple, account_type in zip(output_tuples, original_account_types):
            updated_account, _ = output_tuple
            assert updated_account.account_type == account_type

    def test_create_account_with_alias(
        self,
        saltedge_account: saltedge_client.Account,
        user_foo: User,
        connection_foo: Connection,
    ) -> None:
        saltedge_account.extra.account_name = "account alias"
        saltedge_account.connection_id = connection_foo.external_id
        saltedge_accounts = [saltedge_account]
        output_tuples = import_saltedge_accounts(saltedge_accounts, user_foo)
        for new_account, _ in output_tuples:
            assert new_account.alias == saltedge_account.extra.account_name

    def test_update_account_with_alias(
        self,
        account_foo: Account,
        saltedge_account: saltedge_client.Account,
        user_foo: User,
        connection_foo: Connection,
    ) -> None:
        saltedge_account.extra.account_name = "account alias"
        saltedge_account.connection_id = connection_foo.external_id
        saltedge_accounts = [saltedge_account]
        account_foo.alias = "old alias"
        account_foo.save()
        output_tuples = import_saltedge_accounts(saltedge_accounts, user_foo)
        for updated_account, _ in output_tuples:
            assert updated_account.alias == saltedge_account.extra.account_name


class TestImportSaltedgeTransactions:
    @pytest.fixture
    def saltedge_transactions(
        self,
        saltedge_transaction_factory: Callable[..., saltedge_client.Transaction],
        saltedge_account: saltedge_client.Account,
        account_foo: Account,
    ) -> List[saltedge_client.Transaction]:
        account_foo.external_id = saltedge_account.id
        account_foo.save()
        return [
            saltedge_transaction_factory(
                id="1",
                made_on=datetime.datetime.strptime("2020-01-01", "%Y-%m-%d").date(),
                amount=1.0,
                description="a",
                account_id=saltedge_account.id,
            ),
            saltedge_transaction_factory(
                id="2",
                made_on=datetime.datetime.strptime("2020-01-02", "%Y-%m-%d").date(),
                amount=2.0,
                description="b",
                account_id=saltedge_account.id,
            ),
            saltedge_transaction_factory(
                id="3",
                made_on=datetime.datetime.strptime("2020-01-03", "%Y-%m-%d").date(),
                amount=3.0,
                description="c",
                account_id=saltedge_account.id,
            ),
        ]

    @pytest.fixture
    def transactions(
        self,
        transaction_factory: Callable[..., Transaction],
        saltedge_transactions: List[saltedge_client.Transaction],
    ) -> List[Transaction]:
        transactions = []
        for saltedge_transaction in saltedge_transactions:
            transactions.append(
                transaction_factory(
                    date=saltedge_transaction.made_on + datetime.timedelta(days=10),
                    amount=saltedge_transaction.amount + 10,
                    description=saltedge_transaction.description + "_ tmp",
                    external_id=int(saltedge_transaction.id),
                )
            )
        return transactions

    def test_transactions_are_created(
        self,
        saltedge_transactions: List[saltedge_client.Transaction],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        output_tuples = import_saltedge_transactions(saltedge_transactions, user_foo)
        for output_tuple, saltedge_transaction in zip(
            output_tuples, saltedge_transactions
        ):
            new_transaction, is_created = output_tuple
            assert new_transaction.date == saltedge_transaction.made_on
            assert new_transaction.amount == saltedge_transaction.amount
            assert new_transaction.description == saltedge_transaction.description
            assert new_transaction.user == user_foo
            assert new_transaction.external_id == int(saltedge_transaction.id)
            assert new_transaction.account == account_foo
            assert is_created is True

    def test_transactions_are_updated(
        self,
        transactions: List[Transaction],
        saltedge_transactions: List[saltedge_client.Transaction],
        user_foo: User,
        account_foo: Account,
    ) -> None:
        output_tuples = import_saltedge_transactions(saltedge_transactions, user_foo)
        for output_tuple, saltedge_transaction in zip(
            output_tuples, saltedge_transactions
        ):
            updated_transaction, is_created = output_tuple
            assert updated_transaction.date == saltedge_transaction.made_on
            assert updated_transaction.amount == saltedge_transaction.amount
            assert updated_transaction.description == saltedge_transaction.description
            assert updated_transaction.user == user_foo
            assert updated_transaction.external_id == int(saltedge_transaction.id)
            assert updated_transaction.account == account_foo
            assert is_created is False

    def test_payee_is_not_overriden(
        self,
        transactions: List[Transaction],
        saltedge_transactions: List[saltedge_client.Transaction],
        user_foo: User,
    ) -> None:
        original_peyees = [t.payee for t in transactions]
        output_tuples = import_saltedge_transactions(saltedge_transactions, user_foo)
        for output_tuple, payee in zip(output_tuples, original_peyees):
            updated_transaction, _ = output_tuple
            assert updated_transaction.payee == payee

    def test_category_is_not_overriden(
        self,
        transactions: List[Transaction],
        saltedge_transactions: List[saltedge_client.Transaction],
        user_foo: User,
    ) -> None:
        original_categories = [t.category for t in transactions]
        output_tuples = import_saltedge_transactions(saltedge_transactions, user_foo)
        for output_tuple, category in zip(output_tuples, original_categories):
            updated_transaction, _ = output_tuple
            assert updated_transaction.category == category


class TestCreateInitialBalance:
    def test_no_transactions(
        self, account_foo: Account, saltedge_account: saltedge_client.Account
    ) -> None:
        transaction = create_initial_balance(account_foo, saltedge_account, [])
        assert transaction.date == datetime.date.today()
        assert transaction.amount == saltedge_account.balance
        assert transaction.description == "Initial balance"
        assert transaction.account == account_foo
        assert transaction.user == account_foo.user

    def test_single_transaction(
        self,
        account_foo: Account,
        saltedge_account: saltedge_client.Account,
        saltedge_transaction: saltedge_client.Transaction,
    ) -> None:
        transaction = create_initial_balance(
            account_foo, saltedge_account, [saltedge_transaction]
        )
        assert transaction.date == saltedge_transaction.made_on
        assert (
            transaction.amount == saltedge_account.balance - saltedge_transaction.amount
        )
        assert transaction.description == "Initial balance"
        assert transaction.account == account_foo
        assert transaction.user == account_foo.user

    def test_multiple_transactions(
        self,
        account_foo: Account,
        saltedge_account: saltedge_client.Account,
        saltedge_transaction_factory: Callable[..., saltedge_client.Transaction],
    ) -> None:
        today = datetime.date.today()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        transactions = [
            saltedge_transaction_factory(amount=1.0, made_on=today),
            saltedge_transaction_factory(amount=2.0, made_on=yesterday),
        ]

        transaction = create_initial_balance(
            account_foo, saltedge_account, transactions
        )
        assert transaction.date == yesterday
        assert transaction.amount == saltedge_account.balance - sum(
            t.amount for t in transactions
        )
        assert transaction.description == "Initial balance"
        assert transaction.account == account_foo
        assert transaction.user == account_foo.user


class TestGetIncomeReport:
    def test_output(self, mocker: MockFixture) -> None:
        mocker.patch(
            "budget.services.get_income_record_per_month",
            autospec=True,
            return_value=[],
        )
        mocker.patch(
            "budget.services.get_income_records_summary",
            autospec=True,
            return_value={},
        )
        output = get_income_report([], datetime.date.today(), datetime.date.today())
        assert output == {"records": [], "summary": {}}


class TestGetIncomeRecordPerMonth:
    def test_no_date_range(self, mocker: MockFixture) -> None:
        mocker.patch(
            "budget.services.get_date_range_per_month", autospec=True, return_value=[],
        )

        accounts: List[Account] = []
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        excluded_categories: List[Category] = []

        output = get_income_record_per_month(
            accounts, from_date, to_date, excluded_categories
        )
        assert output == []

    def test_multiple_date_ranges(self, mocker: MockFixture) -> None:
        date = datetime.date.today()
        mocker.patch(
            "budget.services.get_date_range_per_month",
            autospec=True,
            return_value=[(date, date), (date, date)],
        )
        mocker.patch(
            "budget.services.get_income_record", autospec=True, return_value={},
        )

        accounts: List[Account] = []
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        excluded_categories: List[Category] = []

        output = get_income_record_per_month(
            accounts, from_date, to_date, excluded_categories
        )
        assert output == [{}, {}]


class TestGetIncomeRecordsSummary:
    def test_no_entries(self) -> None:
        output = get_income_records_summary([])
        assert output == {
            "from": datetime.date.today(),
            "to": datetime.date.today(),
            "revenue": Decimal(),
            "expenses": Decimal(),
            "income": Decimal(),
        }

    def test_single_entry(self) -> None:
        records = [
            {
                "from": datetime.date.today(),
                "to": datetime.date.today() + datetime.timedelta(days=1),
                "revenue": Decimal(150.0),
                "expenses": Decimal(50.0),
                "income": Decimal(100.0),
            }
        ]
        output = get_income_records_summary(records)
        assert output == records[0]

    def test_multiple_entries(self) -> None:
        records = [
            {
                "from": datetime.date.today(),
                "to": datetime.date.today() + datetime.timedelta(days=1),
                "revenue": Decimal(150.0),
                "expenses": Decimal(50.0),
                "income": Decimal(100.0),
            },
            {
                "from": datetime.date.today() + datetime.timedelta(days=2),
                "to": datetime.date.today() + datetime.timedelta(days=3),
                "revenue": Decimal(250.0),
                "expenses": Decimal(350.0),
                "income": Decimal(-100.0),
            },
        ]
        output = get_income_records_summary(records)
        assert output == {
            "from": records[0]["from"],
            "to": records[-1]["to"],
            "revenue": sum(r["revenue"] for r in records),
            "expenses": sum(r["expenses"] for r in records),
            "income": sum(r["income"] for r in records),
        }


def test_get_income_record(
    account_foo: Account, category_foo: Category, mocker: MockFixture
) -> None:
    revenue = 100.0
    expenses = 50.0
    income = revenue - expenses

    mocker.patch(
        "budget.services.get_income_transactions", autospec=True, return_value=[],
    )
    mocker.patch(
        "budget.services.get_revenue", autospec=True, return_value=revenue,
    )
    mocker.patch(
        "budget.services.get_expenses", autospec=True, return_value=expenses,
    )

    accounts = [account_foo]
    from_date = datetime.date.today()
    to_date = datetime.date.today() + datetime.timedelta(days=1)
    excluded_categories = [category_foo]

    output = get_income_record(accounts, from_date, to_date, excluded_categories)
    assert output == {
        "from": from_date,
        "to": to_date,
        "revenue": revenue,
        "expenses": expenses,
        "income": income,
    }


class TestGetIncomeTransactions:
    def test_no_accounts(self) -> None:
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        output = get_income_transactions([], from_date, to_date)
        assert list(output) == []

    def test_no_transactions(self, account_foo: Account) -> None:
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        output = get_income_transactions([account_foo], from_date, to_date)
        assert list(output) == []

    def test_transactions_before_from_date(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        from_date = datetime.date.today()
        past = from_date - datetime.timedelta(days=1)
        to_date = datetime.date.today()
        transaction_factory(date=past, account=account_foo)
        output = get_income_transactions([account_foo], from_date, to_date)
        assert list(output) == []

    def test_transactions_at_from_date(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        from_date = datetime.date.today()
        to_date = from_date + datetime.timedelta(days=1)
        transactions = [transaction_factory(date=from_date, account=account_foo)]
        output = get_income_transactions([account_foo], from_date, to_date)
        assert list(output) == transactions

    def test_transactions_after_to_date(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        future = to_date + datetime.timedelta(days=1)
        transaction_factory(date=future, account=account_foo)
        output = get_income_transactions([account_foo], from_date, to_date)
        assert list(output) == []

    def test_transactions_at_to_date(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        from_date = datetime.date.today()
        to_date = from_date + datetime.timedelta(days=1)
        transactions = [transaction_factory(date=to_date, account=account_foo)]
        output = get_income_transactions([account_foo], from_date, to_date)
        assert list(output) == transactions

    def test_transactions_between_from_and_to_dates(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        from_date = datetime.date.today()
        date = from_date + datetime.timedelta(days=1)
        to_date = date + datetime.timedelta(days=1)
        transactions = [transaction_factory(date=date, account=account_foo)]
        output = get_income_transactions([account_foo], from_date, to_date)
        assert list(output) == transactions

    def test_different_accounts(
        self,
        account_factory: Callable[..., Account],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        account_a = account_factory(name="a")
        account_b = account_factory(name="b")
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        transactions = [transaction_factory(date=to_date, account=account_a)]
        transaction_factory(date=to_date, account=account_b)
        output = get_income_transactions([account_a], from_date, to_date)
        assert list(output) == transactions

    def test_multiple_accounts(
        self,
        account_factory: Callable[..., Account],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        account_a = account_factory(name="a")
        account_b = account_factory(name="b")
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        transactions = [
            transaction_factory(date=to_date, account=account_a),
            transaction_factory(date=to_date, account=account_b),
        ]
        output = get_income_transactions([account_a, account_b], from_date, to_date)
        assert list(output) == transactions

    def test_excluded_categories(
        self,
        account_foo: Account,
        transaction_factory: Callable[..., Transaction],
        category_factory: Callable[..., Category],
    ) -> None:
        category_a = category_factory(name="a")
        category_b = category_factory(name="b")
        category_c = category_factory(name="c")
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        transactions = [
            transaction_factory(date=to_date, account=account_foo, category=category_a)
        ]
        transaction_factory(date=to_date, account=account_foo, category=category_b)
        transaction_factory(date=to_date, account=account_foo, category=category_c)
        output = get_income_transactions(
            [account_foo], from_date, to_date, [category_b, category_c]
        )
        assert list(output) == transactions


class TestGetRevenue:
    def test_no_transactions(self) -> None:
        output = get_revenue(Transaction.objects.none())
        assert output == Decimal()

    def test_no_revenue(self, transaction_factory: Callable[..., Transaction]) -> None:
        transaction_factory(amount=-100.0)
        output = get_revenue(Transaction.objects.all())
        assert output == Decimal()

    def test_revenue(self, transaction_factory: Callable[..., Transaction]) -> None:
        transactions = [
            transaction_factory(amount=100.0),
            transaction_factory(amount=100.0),
        ]
        output = get_revenue(Transaction.objects.all())
        assert output == sum(t.amount for t in transactions)


class TestGetExpenses:
    def test_no_transactions(self) -> None:
        output = get_expenses(Transaction.objects.none())
        assert output == Decimal()

    def test_no_expenses(self, transaction_factory: Callable[..., Transaction]) -> None:
        transaction_factory(amount=100.0)
        output = get_expenses(Transaction.objects.all())
        assert output == Decimal()

    def test_expenses(self, transaction_factory: Callable[..., Transaction]) -> None:
        transactions = [
            transaction_factory(amount=-100.0),
            transaction_factory(amount=-100.0),
        ]
        output = get_expenses(Transaction.objects.all())
        assert output == abs(sum(t.amount for t in transactions))


class TestGetBalanceReport:
    def test_output(self, mocker: MockFixture) -> None:
        mocker.patch(
            "budget.services.get_balance_record_per_month",
            autospec=True,
            return_value=[],
        )
        mocker.patch(
            "budget.services.get_balance_records_summary",
            autospec=True,
            return_value={},
        )
        output = get_balance_report([], datetime.date.today(), datetime.date.today())
        assert output == {"records": [], "summary": {}}


class TestGetBalanceRecordPerMonth:
    def test_no_date_range(self, mocker: MockFixture) -> None:
        mocker.patch(
            "budget.services.get_date_range_per_month", autospec=True, return_value=[],
        )

        accounts: List[Account] = []
        from_date = datetime.date.today()
        to_date = datetime.date.today()

        output = get_balance_record_per_month(accounts, from_date, to_date)
        assert output == []

    def test_multiple_date_ranges(self, mocker: MockFixture) -> None:
        date = datetime.date.today()
        mocker.patch(
            "budget.services.get_date_range_per_month",
            autospec=True,
            return_value=[(date, date), (date, date)],
        )
        mocker.patch(
            "budget.services.get_balance_record", autospec=True, return_value={},
        )

        accounts: List[Account] = []
        from_date = datetime.date.today()
        to_date = datetime.date.today()

        output = get_balance_record_per_month(accounts, from_date, to_date)
        assert output == [{}, {}]


def test_get_balance_record(account_foo: Account, mocker: MockFixture) -> None:
    opening_balance = 1000
    ending_balance = 1500
    difference = ending_balance - opening_balance

    mocker.patch(
        "budget.services.get_opening_balance",
        autospec=True,
        return_value=opening_balance,
    )
    mocker.patch(
        "budget.services.get_ending_balance",
        autospec=True,
        return_value=ending_balance,
    )

    accounts = [account_foo]
    from_date = datetime.date.today()
    to_date = datetime.date.today() + datetime.timedelta(days=1)

    output = get_balance_record(accounts, from_date, to_date)
    assert output == {
        "from": from_date,
        "to": to_date,
        "opening_balance": opening_balance,
        "ending_balance": ending_balance,
        "difference": difference,
    }


class TestGetOpeningBalance:
    def test_no_transactions(self, account_foo: Account) -> None:
        date = datetime.date.today()
        output = get_opening_balance(date, [account_foo])
        assert output == Decimal()

    def test_transactions_after_date(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        date = datetime.date.today()
        future = date + datetime.timedelta(days=1)
        transaction_factory(date=future, account=account_foo)
        output = get_opening_balance(date, [account_foo])
        assert output == Decimal()

    def test_transactions_at_date(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        date = datetime.date.today()
        transaction_factory(date=date, account=account_foo)
        output = get_opening_balance(date, [account_foo])
        assert output == Decimal()

    def test_transactions_before_date(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        date = datetime.date.today()
        past = date - datetime.timedelta(days=1)
        transactions = [
            transaction_factory(date=past, account=account_foo),
            transaction_factory(date=past, account=account_foo),
        ]
        output = get_opening_balance(date, [account_foo])
        assert output == sum(t.amount for t in transactions)

    def test_transactions_from_different_account(
        self,
        account_factory: Callable[..., Account],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        date = datetime.date.today()
        past = date - datetime.timedelta(days=1)
        account_a = account_factory(name="a")
        account_b = account_factory(name="b")
        transaction_factory(date=past, account=account_a)
        output = get_opening_balance(date, [account_b])
        assert output == Decimal()

    def test_transactions_from_multiple_accounts(
        self,
        account_factory: Callable[..., Account],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        date = datetime.date.today()
        past = date - datetime.timedelta(days=1)
        account_a = account_factory(name="a")
        account_b = account_factory(name="b")
        transactions = [
            transaction_factory(date=past, account=account_a),
            transaction_factory(date=past, account=account_b),
        ]
        output = get_opening_balance(date, [account_a, account_b])
        assert output == sum(t.amount for t in transactions)


class TestGetEndingBalance:
    def test_no_transactions(self, account_foo: Account) -> None:
        date = datetime.date.today()
        output = get_ending_balance(date, [account_foo])
        assert output == Decimal()

    def test_transactions_after_date(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        date = datetime.date.today()
        future = date + datetime.timedelta(days=1)
        transaction_factory(date=future, account=account_foo)
        output = get_ending_balance(date, [account_foo])
        assert output == Decimal()

    def test_transactions_at_date(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        date = datetime.date.today()
        transactions = [transaction_factory(date=date, account=account_foo)]
        output = get_ending_balance(date, [account_foo])
        assert output == sum(t.amount for t in transactions)

    def test_transactions_before_date(
        self, account_foo: Account, transaction_factory: Callable[..., Transaction]
    ) -> None:
        date = datetime.date.today()
        past = date - datetime.timedelta(days=1)
        transactions = [
            transaction_factory(date=past, account=account_foo),
            transaction_factory(date=past, account=account_foo),
        ]
        output = get_ending_balance(date, [account_foo])
        assert output == sum(t.amount for t in transactions)

    def test_transactions_from_different_account(
        self,
        account_factory: Callable[..., Account],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        date = datetime.date.today()
        past = date - datetime.timedelta(days=1)
        account_a = account_factory(name="a")
        account_b = account_factory(name="b")
        transaction_factory(date=past, account=account_a)
        output = get_ending_balance(date, [account_b])
        assert output == Decimal()

    def test_transactions_from_multiple_accounts(
        self,
        account_factory: Callable[..., Account],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        date = datetime.date.today()
        past = date - datetime.timedelta(days=1)
        account_a = account_factory(name="a")
        account_b = account_factory(name="b")
        transactions = [
            transaction_factory(date=past, account=account_a),
            transaction_factory(date=past, account=account_b),
        ]
        output = get_ending_balance(date, [account_a, account_b])
        assert output == sum(t.amount for t in transactions)


class TestGetBalanceRecordsSummary:
    def test_no_entries(self) -> None:
        output = get_balance_records_summary([])
        assert output == {
            "from": datetime.date.today(),
            "to": datetime.date.today(),
            "opening_balance": Decimal(),
            "ending_balance": Decimal(),
            "difference": Decimal(),
        }

    def test_single_entry(self) -> None:
        records = [
            {
                "from": datetime.date.today(),
                "to": datetime.date.today() + datetime.timedelta(days=1),
                "opening_balance": Decimal(1000.0),
                "ending_balance": Decimal(1100.0),
                "difference": Decimal(100.0),
            }
        ]
        output = get_balance_records_summary(records)
        assert output == records[0]

    def test_multiple_entries(self) -> None:
        records = [
            {
                "from": datetime.date.today(),
                "to": datetime.date.today() + datetime.timedelta(days=1),
                "opening_balance": Decimal(1000.0),
                "ending_balance": Decimal(1100.0),
                "difference": Decimal(100.0),
            },
            {
                "from": datetime.date.today() + datetime.timedelta(days=2),
                "to": datetime.date.today() + datetime.timedelta(days=3),
                "opening_balance": Decimal(2000.0),
                "ending_balance": Decimal(1900.0),
                "difference": Decimal(-100.0),
            },
        ]
        output = get_balance_records_summary(records)
        assert output == {
            "from": records[0]["from"],
            "to": records[-1]["to"],
            "opening_balance": records[0]["opening_balance"],
            "ending_balance": records[-1]["ending_balance"],
            # For some reason mypy can't deduce that ending_balance is Decimal
            "difference": records[-1]["ending_balance"] - records[0]["opening_balance"],  # type: ignore
        }


class TestGetDateRangePerMonth:
    def test_from_date_and_end_date_are_the_same(self) -> None:
        assert get_date_range_per_month(
            datetime.date(2020, 1, 2), datetime.date(2020, 1, 2)
        ) == [(datetime.date(2020, 1, 2), datetime.date(2020, 1, 2))]

    def test_from_date_and_end_date_in_the_same_month(self) -> None:
        assert get_date_range_per_month(
            datetime.date(2020, 1, 2), datetime.date(2020, 1, 15)
        ) == [(datetime.date(2020, 1, 2), datetime.date(2020, 1, 15))]

    def test_from_date_and_end_date_within_one_month_31_days(self) -> None:
        assert get_date_range_per_month(
            datetime.date(2020, 1, 2), datetime.date(2020, 2, 15)
        ) == [
            (datetime.date(2020, 1, 2), datetime.date(2020, 1, 31)),
            (datetime.date(2020, 2, 1), datetime.date(2020, 2, 15)),
        ]

    def test_from_date_and_end_date_within_one_month_30_days(self) -> None:
        assert get_date_range_per_month(
            datetime.date(2020, 4, 2), datetime.date(2020, 5, 15)
        ) == [
            (datetime.date(2020, 4, 2), datetime.date(2020, 4, 30)),
            (datetime.date(2020, 5, 1), datetime.date(2020, 5, 15)),
        ]

    def test_from_date_and_end_date_within_one_month_29_days(self) -> None:
        assert get_date_range_per_month(
            datetime.date(2020, 2, 2), datetime.date(2020, 3, 15)
        ) == [
            (datetime.date(2020, 2, 2), datetime.date(2020, 2, 29)),
            (datetime.date(2020, 3, 1), datetime.date(2020, 3, 15)),
        ]

    def test_from_date_and_end_date_within_one_month_28_days(self) -> None:
        assert get_date_range_per_month(
            datetime.date(2021, 2, 2), datetime.date(2021, 3, 15)
        ) == [
            (datetime.date(2021, 2, 2), datetime.date(2021, 2, 28)),
            (datetime.date(2021, 3, 1), datetime.date(2021, 3, 15)),
        ]

    def test_from_date_and_end_date_within_multiple_months(self) -> None:
        assert get_date_range_per_month(
            datetime.date(2020, 3, 2), datetime.date(2020, 6, 15)
        ) == [
            (datetime.date(2020, 3, 2), datetime.date(2020, 3, 31)),
            (datetime.date(2020, 4, 1), datetime.date(2020, 4, 30)),
            (datetime.date(2020, 5, 1), datetime.date(2020, 5, 31)),
            (datetime.date(2020, 6, 1), datetime.date(2020, 6, 15)),
        ]

    def test_from_date_and_end_date_with_different_years(self) -> None:
        assert get_date_range_per_month(
            datetime.date(2020, 12, 2), datetime.date(2021, 1, 15)
        ) == [
            (datetime.date(2020, 12, 2), datetime.date(2020, 12, 31)),
            (datetime.date(2021, 1, 1), datetime.date(2021, 1, 15)),
        ]


class TestDiffMonth:
    def test_from_and_to_date_are_the_same(self) -> None:
        assert diff_month(datetime.date(2020, 1, 2), datetime.date(2020, 1, 2)) == 0

    def test_from_date_before_to_date(self) -> None:
        assert diff_month(datetime.date(2020, 1, 2), datetime.date(2020, 3, 4)) == -2

    def test_from_date_after_to_date(self) -> None:
        assert diff_month(datetime.date(2020, 3, 4), datetime.date(2020, 1, 2)) == 2

    def test_dates_with_the_same_month_and_different_days(self) -> None:
        assert diff_month(datetime.date(2020, 1, 2), datetime.date(2020, 1, 3)) == 0

    def test_dates_with_the_same_month_day_and_different_year(self) -> None:
        assert diff_month(datetime.date(2020, 1, 2), datetime.date(2022, 1, 2)) == -24


class TestAddMonth:
    def test_regular_input(self) -> None:
        assert add_month(datetime.date(2020, 3, 5)) == datetime.date(2020, 4, 5)

    def test_input_date_in_december(self) -> None:
        assert add_month(datetime.date(2020, 12, 2)) == datetime.date(2021, 1, 2)

    def test_input_date_with_more_days_than_output(self) -> None:
        assert add_month(datetime.date(2020, 3, 31)) == datetime.date(2020, 4, 30)


class TestGetMonthStart:
    def test_input_date_already_at_start(self) -> None:
        assert get_month_start(datetime.date(2020, 2, 1)) == datetime.date(2020, 2, 1)

    def test_input_date_not_at_start(self) -> None:
        assert get_month_start(datetime.date(2020, 2, 3)) == datetime.date(2020, 2, 1)


class TestGetMonthEnd:
    def test_input_date_already_at_end(self) -> None:
        assert get_month_end(datetime.date(2020, 1, 31)) == datetime.date(2020, 1, 31)

    def test_input_date_not_at_end(self) -> None:
        assert get_month_end(datetime.date(2020, 1, 2)) == datetime.date(2020, 1, 31)

    def test_month_with_31_days(self) -> None:
        assert get_month_end(datetime.date(2020, 1, 2)) == datetime.date(2020, 1, 31)

    def test_month_with_30_days(self) -> None:
        assert get_month_end(datetime.date(2020, 4, 2)) == datetime.date(2020, 4, 30)

    def test_month_with_29_days(self) -> None:
        assert get_month_end(datetime.date(2020, 2, 2)) == datetime.date(2020, 2, 29)

    def test_month_with_28_days(self) -> None:
        assert get_month_end(datetime.date(2021, 2, 2)) == datetime.date(2021, 2, 28)


class TestGetCategoryBalance:
    def test_no_transactions(
        self,
        account_foo: Account,
        transaction_factory: Callable[..., Transaction],
        category_factory: Callable[..., Category],
    ) -> None:
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        category_foo = category_factory(name="foo", user=account_foo.user)
        category_bar = category_factory(name="bar", user=account_foo.user)
        transaction_factory(
            account=account_foo,
            user=account_foo.user,
            date=from_date,
            amount=Decimal(100.0),
        )
        transaction_factory(
            account=account_foo,
            user=account_foo.user,
            date=from_date,
            amount=Decimal(200.0),
            category=category_foo,
        )
        output = get_category_balance(category_bar, [account_foo], from_date, to_date)
        assert output == Decimal()

    def test_single_transaction(
        self,
        account_foo: Account,
        transaction_factory: Callable[..., Transaction],
        category_foo: Category,
    ) -> None:
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        transaction = transaction_factory(
            account=account_foo,
            user=account_foo.user,
            date=from_date,
            amount=Decimal(-150.0),
            category=category_foo,
        )
        output = get_category_balance(category_foo, [account_foo], from_date, to_date)
        assert output == transaction.amount

    def test_multiple_transactions(
        self,
        account_foo: Account,
        transaction_factory: Callable[..., Transaction],
        category_foo: Category,
    ) -> None:
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        transactions = [
            transaction_factory(
                account=account_foo,
                user=account_foo.user,
                date=from_date,
                amount=Decimal(-150.0),
                category=category_foo,
            ),
            transaction_factory(
                account=account_foo,
                user=account_foo.user,
                date=from_date,
                amount=Decimal(200.0),
                category=category_foo,
            ),
        ]
        output = get_category_balance(category_foo, [account_foo], from_date, to_date)
        assert output == sum(t.amount for t in transactions)

    def test_transactions_before_from_date(
        self,
        account_foo: Account,
        transaction_factory: Callable[..., Transaction],
        category_foo: Category,
    ) -> None:
        from_date = datetime.date.today()
        past = from_date - datetime.timedelta(days=1)
        to_date = datetime.date.today()
        transaction_factory(
            account=account_foo,
            user=account_foo.user,
            date=past,
            amount=Decimal(-150.0),
            category=category_foo,
        )
        output = get_category_balance(category_foo, [account_foo], from_date, to_date)
        assert output == Decimal()

    def test_transactions_after_to_date(
        self,
        account_foo: Account,
        transaction_factory: Callable[..., Transaction],
        category_foo: Category,
    ) -> None:
        from_date = datetime.date.today()
        to_date = datetime.date.today()
        future = to_date + datetime.timedelta(days=1)
        transaction_factory(
            account=account_foo,
            user=account_foo.user,
            date=future,
            amount=Decimal(-150.0),
            category=category_foo,
        )
        output = get_category_balance(category_foo, [account_foo], from_date, to_date)
        assert output == Decimal()


class TestGetCategoryBalanceRecordPerMonth:
    def test_no_date_range(self, category_foo: Category, mocker: MockFixture) -> None:
        mocker.patch(
            "budget.services.get_date_range_per_month", autospec=True, return_value=[],
        )

        categories: List[Category] = [category_foo]
        accounts: List[Account] = []
        from_date = datetime.date.today()
        to_date = datetime.date.today()

        output = get_category_balance_record_per_month(
            categories, accounts, from_date, to_date
        )
        assert output == []

    def test_single_date_range(
        self, category_foo: Category, mocker: MockFixture
    ) -> None:
        date_range = (
            datetime.date.today(),
            datetime.date.today() + datetime.timedelta(days=1),
        )
        mocker.patch(
            "budget.services.get_date_range_per_month",
            autospec=True,
            return_value=[date_range],
        )
        mocker.patch(
            "budget.services.get_category_balance", autospec=True, return_value=123,
        )

        categories: List[Category] = [category_foo]
        accounts: List[Account] = []
        from_date = datetime.date.today()
        to_date = datetime.date.today()

        output = get_category_balance_record_per_month(
            categories, accounts, from_date, to_date
        )
        assert output == [
            {"from": date_range[0], "to": date_range[1], category_foo.name: 123}
        ]

    def test_multiple_date_ranges(
        self, category_foo: Category, mocker: MockFixture
    ) -> None:
        date_ranges = [
            (datetime.date.today(), datetime.date.today() + datetime.timedelta(days=1)),
            (
                datetime.date.today() + datetime.timedelta(days=2),
                datetime.date.today() + datetime.timedelta(days=3),
            ),
        ]
        mocker.patch(
            "budget.services.get_date_range_per_month",
            autospec=True,
            return_value=date_ranges,
        )
        mocker.patch(
            "budget.services.get_category_balance",
            autospec=True,
            side_effect=[123, 456],
        )

        categories: List[Category] = [category_foo]
        accounts: List[Account] = []
        from_date = datetime.date.today()
        to_date = datetime.date.today()

        output = get_category_balance_record_per_month(
            categories, accounts, from_date, to_date
        )
        assert output == [
            {
                "from": date_ranges[0][0],
                "to": date_ranges[0][1],
                category_foo.name: 123,
            },
            {
                "from": date_ranges[1][0],
                "to": date_ranges[1][1],
                category_foo.name: 456,
            },
        ]

    def test_multiple_categories(
        self, category_factory: Callable[..., Category], mocker: MockFixture
    ) -> None:
        date_range = (
            datetime.date.today(),
            datetime.date.today() + datetime.timedelta(days=1),
        )
        mocker.patch(
            "budget.services.get_date_range_per_month",
            autospec=True,
            return_value=[date_range],
        )
        mocker.patch(
            "budget.services.get_category_balance",
            autospec=True,
            side_effect=[123, 456],
        )

        categories: List[Category] = [
            category_factory(name="a"),
            category_factory(name="b"),
        ]
        accounts: List[Account] = []
        from_date = datetime.date.today()
        to_date = datetime.date.today()

        output = get_category_balance_record_per_month(
            categories, accounts, from_date, to_date
        )
        assert output == [
            {
                "from": date_range[0],
                "to": date_range[1],
                categories[0].name: 123,
                categories[1].name: 456,
            }
        ]


class TestGetCategoryBalanceReport:
    def test_output(self, mocker: MockFixture) -> None:
        mocker.patch(
            "budget.services.get_category_balance_report_header",
            autospec=True,
            return_value=[],
        )
        mocker.patch(
            "budget.services.get_category_balance_record_per_month",
            autospec=True,
            return_value=[],
        )
        mocker.patch(
            "budget.services.get_category_balance_records_summary",
            autospec=True,
            return_value={},
        )
        output = get_category_balance_report(
            [], [], datetime.date.today(), datetime.date.today()
        )
        assert output == {"header": [], "records": [], "summary": {}}


class TestGetCategoryBalanceReportHeader:
    def test_no_categories(self) -> None:
        output = get_category_balance_report_header([])
        assert output == ["From", "To"]

    def test_single_category(self, category_foo: Category) -> None:
        output = get_category_balance_report_header([category_foo])
        assert output == ["From", "To", category_foo.name]

    def test_multiple_categories(
        self, category_factory: Callable[..., Category]
    ) -> None:
        categories = [category_factory(name="a"), category_factory(name="b")]
        output = get_category_balance_report_header(categories)
        assert output == ["From", "To", categories[0].name, categories[1].name]


class TestGetCategoryBalanceRecordsSummary:
    def test_no_entries(self) -> None:
        output = get_category_balance_records_summary([])
        assert output == {
            "from": datetime.date.today(),
            "to": datetime.date.today(),
        }

    def test_single_entry(self) -> None:
        records = [
            {
                "from": datetime.date.today(),
                "to": datetime.date.today() + datetime.timedelta(days=1),
                "category_a": Decimal(150.0),
                "category_b": Decimal(-150.0),
            }
        ]
        output = get_category_balance_records_summary(records)
        assert output == records[0]

    def test_multiple_entries(self) -> None:
        records = [
            {
                "from": datetime.date.today(),
                "to": datetime.date.today() + datetime.timedelta(days=1),
                "category_a": Decimal(150.0),
                "category_b": Decimal(-150.0),
            },
            {
                "from": datetime.date.today(),
                "to": datetime.date.today() + datetime.timedelta(days=1),
                "category_a": Decimal(50.0),
                "category_b": Decimal(150.0),
            },
        ]
        output = get_category_balance_records_summary(records)
        assert output == {
            "from": records[0]["from"],
            "to": records[-1]["to"],
            "category_a": sum(r["category_a"] for r in records),
            "category_b": sum(r["category_b"] for r in records),
        }


class TestFilterTransactions:
    def test_no_transactions(self, user_foo: User) -> None:
        output = filter_transactions(user_foo)
        assert list(output) == list(Transaction.objects.none())

    def test_user_transactions(
        self, user_foo: User, transaction_factory: Callable[..., Transaction]
    ) -> None:
        transactions = [
            transaction_factory(description="foo", user=user_foo),
            transaction_factory(description="bar", user=user_foo),
        ]
        output = filter_transactions(user_foo)
        assert list(output) == transactions

    def test_different_users(
        self,
        user_factory: Callable[..., User],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        user_a = user_factory(username="a")
        user_b = user_factory(username="b")
        transactions = [
            transaction_factory(description="a", user=user_a),
        ]
        transaction_factory(description="b", user=user_b)
        output = filter_transactions(user_a)
        assert list(output) == transactions

    def test_valid_filter_from_date(
        self, user_foo: User, transaction_factory: Callable[..., Transaction]
    ) -> None:
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        tomorrow = today + datetime.timedelta(days=1)
        transactions = [
            transaction_factory(description="foo", date=yesterday, user=user_foo),
            transaction_factory(description="bar", date=today, user=user_foo),
            transaction_factory(description="baz", date=tomorrow, user=user_foo),
        ]
        output = filter_transactions(user_foo, from_date=today)
        assert list(output) == transactions[1:3]

    def test_valid_filter_to_date(
        self, user_foo: User, transaction_factory: Callable[..., Transaction]
    ) -> None:
        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        tomorrow = today + datetime.timedelta(days=1)
        transactions = [
            transaction_factory(description="foo", date=yesterday, user=user_foo),
            transaction_factory(description="bar", date=today, user=user_foo),
            transaction_factory(description="baz", date=tomorrow, user=user_foo),
        ]
        output = filter_transactions(user_foo, to_date=today)
        assert list(output) == transactions[0:2]

    def test_valid_filter_min_amount(
        self, user_foo: User, transaction_factory: Callable[..., Transaction]
    ) -> None:
        transactions = [
            transaction_factory(description="foo", amount=100, user=user_foo),
            transaction_factory(description="bar", amount=200, user=user_foo),
            transaction_factory(description="baz", amount=300, user=user_foo),
        ]
        output = filter_transactions(user_foo, min_amount=200)
        assert list(output) == transactions[1:3]

    def test_valid_filter_max_amount(
        self, user_foo: User, transaction_factory: Callable[..., Transaction]
    ) -> None:
        transactions = [
            transaction_factory(description="foo", amount=100, user=user_foo),
            transaction_factory(description="bar", amount=200, user=user_foo),
            transaction_factory(description="baz", amount=300, user=user_foo),
        ]
        output = filter_transactions(user_foo, max_amount=200)
        assert list(output) == transactions[0:2]

    def test_valid_filter_categories(
        self,
        user_foo: User,
        transaction_factory: Callable[..., Transaction],
        category_factory: Callable[..., Category],
    ) -> None:
        categories = [
            category_factory("a"),
            category_factory("b"),
            category_factory("c"),
        ]
        transactions = [
            transaction_factory(
                description="foo", category=categories[0], user=user_foo
            ),
            transaction_factory(
                description="bar", category=categories[1], user=user_foo
            ),
            transaction_factory(
                description="baz", category=categories[2], user=user_foo
            ),
        ]
        output = filter_transactions(
            user_foo, categories=[categories[0], categories[1]]
        )
        assert list(output) == transactions[0:2]

    def test_valid_filter_description(
        self, user_foo: User, transaction_factory: Callable[..., Transaction]
    ) -> None:
        transactions = [
            transaction_factory(description="foo", user=user_foo),
            transaction_factory(description="xxfooxx", user=user_foo),
            transaction_factory(description="a foo b", user=user_foo),
            transaction_factory(description="FOO", user=user_foo),
            transaction_factory(description="bar", user=user_foo),
        ]
        output = filter_transactions(user_foo, description="foo")
        assert list(output) == transactions[0:4]

    def test_valid_filter_accounts(
        self,
        user_foo: User,
        transaction_factory: Callable[..., Transaction],
        account_factory: Callable[..., Account],
    ) -> None:
        accounts = [
            account_factory("a"),
            account_factory("b"),
            account_factory("c"),
        ]
        transactions = [
            transaction_factory(description="foo", account=accounts[0], user=user_foo),
            transaction_factory(description="bar", account=accounts[1], user=user_foo),
            transaction_factory(description="baz", account=accounts[2], user=user_foo),
        ]
        output = filter_transactions(user_foo, accounts=[accounts[0], accounts[1]])
        assert list(output) == transactions[0:2]

    def test_invalid_filters(
        self, user_foo: User, transaction_factory: Callable[..., Transaction]
    ) -> None:
        transactions = [
            transaction_factory(description="foo", amount=50, user=user_foo),
            transaction_factory(description="foo", amount=100, user=user_foo),
            transaction_factory(description="foo", amount=200, user=user_foo),
            transaction_factory(description="bar", amount=300, user=user_foo),
        ]
        output = filter_transactions(
            user_foo, description="foo", description__asdf="asdf", foo=9000
        )
        assert list(output) == transactions[0:3]


class TestQueryDictToTransactionFilterQuery:
    def test_empty_dict(self) -> None:
        d = QueryDict()
        output = query_dict_to_transaction_filter_query(d)
        assert output == {}

    def test_from_date_empty(self) -> None:
        d = QueryDict("from_date=")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {}

    def test_from_date(self) -> None:
        d = QueryDict("from_date=2020-01-02")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {"from_date": "2020-01-02"}

    def test_to_date_empty(self) -> None:
        d = QueryDict("to_date=")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {}

    def test_to_date(self) -> None:
        d = QueryDict("to_date=2020-01-02")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {"to_date": "2020-01-02"}

    def test_min_amount_empty(self) -> None:
        d = QueryDict("min_amount=")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {}

    def test_min_amount(self) -> None:
        d = QueryDict("min_amount=200.00")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {"min_amount": "200.00"}

    def test_max_amount_empty(self) -> None:
        d = QueryDict("max_amount=")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {}

    def test_max_amount(self) -> None:
        d = QueryDict("max_amount=200.00")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {"max_amount": "200.00"}

    def test_categories_empty(self) -> None:
        d = QueryDict("categories=")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {}

    def test_categoires_single(self) -> None:
        d = QueryDict("categories=1")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {"categories": ["1"]}

    def test_categoires_multiple(self) -> None:
        d = QueryDict("categories=1&categories=10")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {"categories": ["1", "10"]}

    def test_description_empty(self) -> None:
        d = QueryDict("description=")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {}

    def test_description(self) -> None:
        d = QueryDict("description=foo")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {"description": "foo"}

    def test_accountes_empty(self) -> None:
        d = QueryDict("accounts=")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {}

    def test_accounts_single(self) -> None:
        d = QueryDict("accounts=1")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {"accounts": ["1"]}

    def test_accounts_multiple(self) -> None:
        d = QueryDict("accounts=1&accounts=10")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {"accounts": ["1", "10"]}

    def test_all_keys(self) -> None:
        d = QueryDict(
            "from_date=2020-01-01&to_date=2020-02-01&min_amount=100.00&max_amount=200.00&categories=1&description=foo&accounts=1&accounts=2"
        )
        output = query_dict_to_transaction_filter_query(d)
        assert output == {
            "from_date": "2020-01-01",
            "to_date": "2020-02-01",
            "min_amount": "100.00",
            "max_amount": "200.00",
            "categories": ["1"],
            "description": "foo",
            "accounts": ["1", "2"],
        }

    def test_invalid_key(self) -> None:
        d = QueryDict("foo=bar")
        output = query_dict_to_transaction_filter_query(d)
        assert output == {}


class TestTransactionFilterQueryToQueryDict:
    def test_empty_dict(self) -> None:
        d: Dict[str, Any] = {}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict()

    def test_from_date(self) -> None:
        d = {"from_date": "2020-01-02"}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict("from_date=2020-01-02")

    def test_to_date(self) -> None:
        d = {"to_date": "2020-01-02"}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict("to_date=2020-01-02")

    def test_min_amount(self) -> None:
        d = {"min_amount": "200.00"}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict("min_amount=200.00")

    def test_max_amount(self) -> None:
        d = {"max_amount": "200.00"}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict("max_amount=200.00")

    def test_categoires_single(self) -> None:
        d = {"categories": ["1"]}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict("categories=1")

    def test_categoires_multiple(self) -> None:
        d = {"categories": ["1", "10"]}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict("categories=1&categories=10")

    def test_description(self) -> None:
        d = {"description": "foo"}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict("description=foo")

    def test_accounts_single(self) -> None:
        d = {"accounts": ["1"]}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict("accounts=1")

    def test_accounts_multiple(self) -> None:
        d = {"accounts": ["1", "10"]}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict("accounts=1&accounts=10")

    def test_all_keys(self) -> None:
        d = {
            "from_date": "2020-01-01",
            "to_date": "2020-02-01",
            "min_amount": "100.00",
            "max_amount": "200.00",
            "categories": ["1"],
            "description": "foo",
            "accounts": ["1", "2"],
        }
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict(
            "from_date=2020-01-01&to_date=2020-02-01&min_amount=100.00&max_amount=200.00&categories=1&description=foo&accounts=1&accounts=2"
        )

    def test_invalid_key(self) -> None:
        d = {"foo": "bar"}
        output = transaction_filter_query_to_query_dict(d)
        assert output == QueryDict()
