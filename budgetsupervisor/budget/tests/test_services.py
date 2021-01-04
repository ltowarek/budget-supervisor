import datetime
from typing import Callable, List

import pytest
import swagger_client as saltedge_client
from budget.models import Account, Category, Connection, Transaction
from budget.services import (
    create_initial_balance,
    get_category_balance,
    import_saltedge_accounts,
    import_saltedge_connection,
    import_saltedge_connections,
    import_saltedge_transactions,
)
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


class TestGetCategoryBalance:
    def test_filter_by_user(
        self,
        user_factory: Callable[..., User],
        account_factory: Callable[..., Account],
        category_factory: Callable[..., Category],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        user_abc = user_factory("abc")
        user_xyz = user_factory("xyz")

        account_abc = account_factory("abc", user=user_abc)
        account_xyz = account_factory("xyz", user=user_xyz)

        category_abc = category_factory("abc", user_abc)
        category_xyz = category_factory("xyz", user_xyz)

        transaction_factory(
            amount=123.00, account=account_abc, user=user_abc, category=category_abc
        )
        transaction_factory(
            amount=256.00, account=account_xyz, user=user_xyz, category=category_xyz
        )

        output = get_category_balance(
            accounts=[account_abc, account_xyz], user=user_abc,
        )

        assert output == {"abc": 123.00, "Total": 123.00}

    def test_filter_by_account(
        self,
        user_factory: Callable[..., User],
        account_factory: Callable[..., Account],
        category_factory: Callable[..., Category],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        user_abc = user_factory("abc")

        account_abc_1 = account_factory("abc_1", user=user_abc)
        account_abc_2 = account_factory("abc_2", user=user_abc)
        account_abc_3 = account_factory("abc_3", user=user_abc)

        category_abc = category_factory("abc", user_abc)

        transaction_factory(
            amount=4.00, account=account_abc_1, user=user_abc, category=category_abc
        )
        transaction_factory(
            amount=5.00, account=account_abc_2, user=user_abc, category=category_abc
        )
        transaction_factory(
            amount=6.00, account=account_abc_3, user=user_abc, category=category_abc
        )

        output = get_category_balance(
            accounts=[account_abc_1, account_abc_2], user=user_abc,
        )

        assert output == {"abc": 4.00 + 5.00, "Total": 4.00 + 5.00}

    def test_balance_per_category(
        self,
        user_factory: Callable[..., User],
        account_factory: Callable[..., Account],
        category_factory: Callable[..., Category],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        user_abc = user_factory("abc")
        account_abc = account_factory("abc", user=user_abc)
        category_abc_1 = category_factory("abc_1", user_abc)
        category_abc_2 = category_factory("abc_2", user_abc)

        transaction_factory(
            amount=4.00, account=account_abc, user=user_abc, category=category_abc_1
        )
        transaction_factory(
            amount=5.00, account=account_abc, user=user_abc, category=category_abc_2
        )

        output = get_category_balance(accounts=[account_abc], user=user_abc,)

        assert output == {"abc_1": 4.00, "abc_2": 5.00, "Total": 4.00 + 5.00}

    def test_filter_by_from_date(
        self,
        user_factory: Callable[..., User],
        account_factory: Callable[..., Account],
        category_factory: Callable[..., Category],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        user_abc = user_factory("abc")
        account_abc = account_factory("abc", user=user_abc)
        category_abc = category_factory("abc", user_abc)

        transaction_factory(
            amount=4.00,
            account=account_abc,
            date=datetime.date(2020, 2, 1),
            user=user_abc,
            category=category_abc,
        )
        transaction_factory(
            amount=5.00,
            account=account_abc,
            date=datetime.date(2020, 3, 1),
            user=user_abc,
            category=category_abc,
        )
        transaction_factory(
            amount=6.00,
            account=account_abc,
            date=datetime.date(2020, 4, 1),
            user=user_abc,
            category=category_abc,
        )

        output = get_category_balance(
            accounts=[account_abc], user=user_abc, from_date=datetime.date(2020, 3, 1)
        )

        assert output == {"abc": 5.00 + 6.00, "Total": 5.00 + 6.00}

    def test_filter_by_to_date(
        self,
        user_factory: Callable[..., User],
        account_factory: Callable[..., Account],
        category_factory: Callable[..., Category],
        transaction_factory: Callable[..., Transaction],
    ) -> None:
        user_abc = user_factory("abc")
        account_abc = account_factory("abc", user=user_abc)
        category_abc = category_factory("abc", user_abc)

        transaction_factory(
            amount=4.00,
            account=account_abc,
            date=datetime.date(2020, 2, 1),
            user=user_abc,
            category=category_abc,
        )
        transaction_factory(
            amount=5.00,
            account=account_abc,
            date=datetime.date(2020, 3, 1),
            user=user_abc,
            category=category_abc,
        )
        transaction_factory(
            amount=6.00,
            account=account_abc,
            date=datetime.date(2020, 4, 1),
            user=user_abc,
            category=category_abc,
        )

        output = get_category_balance(
            accounts=[account_abc], user=user_abc, to_date=datetime.date(2020, 3, 1)
        )

        assert output == {"abc": 4.00 + 5.00, "Total": 4.00 + 5.00}
