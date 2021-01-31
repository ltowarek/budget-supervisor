import datetime

import pytest
import swagger_client as saltedge_client
from saltedge_wrapper.factory import (
    accounts_api,
    connect_sessions_api,
    connections_api,
    transactions_api,
)
from saltedge_wrapper.utils import (
    create_connect_session,
    get_accounts,
    get_connection,
    get_connections,
    get_pending_transactions,
    get_transactions,
    refresh_connection_in_saltedge,
)

pytestmark = pytest.mark.saltedge


def test_create_connect_session(predefined_customer: saltedge_client.Customer) -> None:
    redirect = "http://www.example.com"
    url = create_connect_session(
        redirect, predefined_customer.id, connect_sessions_api()
    )
    assert "https://www.saltedge.com/connect?token=" in url


def test_create_connect_session_with_from_date(
    predefined_customer: saltedge_client.Customer,
) -> None:
    redirect = "http://www.example.com"
    url = create_connect_session(
        redirect,
        predefined_customer.id,
        connect_sessions_api(),
        from_date=datetime.date.today(),
    )
    assert "https://www.saltedge.com/connect?token=" in url


def test_create_connect_session_with_from_date_365_days_ago(
    predefined_customer: saltedge_client.Customer,
) -> None:
    redirect = "http://www.example.com"
    url = create_connect_session(
        redirect,
        predefined_customer.id,
        connect_sessions_api(),
        from_date=datetime.date.today() - datetime.timedelta(days=365),
    )
    assert "https://www.saltedge.com/connect?token=" in url


def test_create_connect_session_with_to_date(
    predefined_customer: saltedge_client.Customer,
) -> None:
    redirect = "http://www.example.com"
    url = create_connect_session(
        redirect,
        predefined_customer.id,
        connect_sessions_api(),
        to_date=datetime.date.today(),
    )
    assert "https://www.saltedge.com/connect?token=" in url


def test_create_connect_session_with_from_and_to_date(
    predefined_customer: saltedge_client.Customer,
) -> None:
    redirect = "http://www.example.com"
    url = create_connect_session(
        redirect,
        predefined_customer.id,
        connect_sessions_api(),
        from_date=datetime.date.today(),
        to_date=datetime.date.today(),
    )
    assert "https://www.saltedge.com/connect?token=" in url


def test_get_connection(
    predefined_saltedge_connection: saltedge_client.Connection,
) -> None:
    connection = get_connection(predefined_saltedge_connection.id, connections_api())
    assert connection == predefined_saltedge_connection


def test_get_connections(
    predefined_customer: saltedge_client.Customer,
    predefined_saltedge_connection: saltedge_client.Connection,
) -> None:
    connections = get_connections(predefined_customer.id, connections_api())
    assert connections == [predefined_saltedge_connection]


def test_refresh_connection(
    predefined_saltedge_connection: saltedge_client.Connection,
) -> None:
    redirect = "http://www.example.com"
    url = refresh_connection_in_saltedge(
        redirect, predefined_saltedge_connection.id, connect_sessions_api()
    )
    assert "https://www.saltedge.com/connect?token=" in url


@pytest.mark.skip(reason="impossible to test without selenium")
def test_remove_connection() -> None:
    pass


def test_get_accounts(
    predefined_saltedge_connection: saltedge_client.Connection,
) -> None:
    accounts = get_accounts(predefined_saltedge_connection.id, accounts_api())
    assert len(accounts) == 5


def test_get_transactions(
    predefined_saltedge_connection: saltedge_client.Connection,
    predefined_saltedge_account: saltedge_client.Account,
) -> None:
    transactions = get_transactions(
        predefined_saltedge_connection.id,
        predefined_saltedge_account.id,
        transactions_api(),
    )
    assert len(transactions) == 5


def test_get_pending_transactions(
    predefined_saltedge_connection: saltedge_client.Connection,
    predefined_saltedge_account: saltedge_client.Account,
) -> None:
    transactions = get_pending_transactions(
        predefined_saltedge_connection.id,
        predefined_saltedge_account.id,
        transactions_api(),
    )
    assert len(transactions) == 0
