from .mocks import MockSaltEdgeWrapper
from ..wrapper import SaltEdgeWrapper
import os
import pytest


pytestmark = pytest.mark.webtest


@pytest.fixture
def actual_saltedge_factory():
    def create_wrapper(app_id, secret, private_path):
        return SaltEdgeWrapper(app_id, secret, private_path)

    return create_wrapper


@pytest.fixture
def actual_saltedge(actual_saltedge_factory):
    app_id = os.environ["APP_ID"]
    secret = os.environ["SECRET"]
    private_path = "saltedge/private.pem"
    return actual_saltedge_factory(app_id, secret, private_path)


@pytest.fixture
def actual_customer_factory(actual_saltedge):
    created_ids = []

    def create_customer(identifier):
        response = actual_saltedge.create_customer(identifier)
        customer = response["data"]
        created_ids.append(customer["id"])
        return response

    yield create_customer

    existing_ids = [c["id"] for c in actual_saltedge.list_customers()["data"]]
    for id in created_ids:
        if id in existing_ids:
            actual_saltedge.remove_customer(id)


@pytest.fixture
def actual_customer_1234(actual_customer_factory):
    return actual_customer_factory("test_1234")["data"]


@pytest.fixture
def mocked_customer_1234(mock_saltedge):
    return mock_saltedge.create_customer("test_1234")["data"]


@pytest.fixture
def predefined_customer(actual_saltedge):
    return actual_saltedge.show_customer(os.environ["CUSTOMER_ID"])["data"]


@pytest.fixture
def predefined_connection(actual_saltedge):
    return actual_saltedge.show_connection(os.environ["CONNECTION_ID"])["data"]


@pytest.fixture
def mocked_connection_1234(mock_saltedge, mocked_customer_1234):
    return mock_saltedge.create_connection(mocked_customer_1234["id"])["data"]


@pytest.fixture
def predefined_account(actual_saltedge, predefined_connection):
    return actual_saltedge.list_accounts(predefined_connection["id"])["data"][0]


@pytest.fixture
def mocked_account_1234(mock_saltedge, mocked_connection_1234):
    return mock_saltedge.create_account(mocked_connection_1234["id"])


def check_customer_schema(customer):
    assert ["id", "identifier", "secret"] == list(customer.keys())


def check_connection_schema(connection):
    assert [
        "id",
        "secret",
        "provider_id",
        "provider_code",
        "provider_name",
        "customer_id",
        "next_refresh_possible_at",
        "created_at",
        "updated_at",
        "status",
        "categorization",
        "daily_refresh",
        "store_credentials",
        "country_code",
        "last_success_at",
        "show_consent_confirmation",
        "last_consent_id",
        "last_attempt",
    ] == list(connection.keys())


def check_account_schema(account):
    assert [
        "id",
        "connection_id",
        "name",
        "nature",
        "balance",
        "currency_code",
        "extra",
        "created_at",
        "updated_at",
    ] == list(account.keys())


def check_transaction_schema(transaction):
    assert [
        "id",
        "account_id",
        "duplicated",
        "mode",
        "status",
        "made_on",
        "amount",
        "currency_code",
        "description",
        "category",
        "extra",
        "created_at",
        "updated_at",
    ] == list(transaction.keys())


def test_create_customer_successfully(mock_saltedge, actual_customer_factory):
    identifier = "test"
    actual = actual_customer_factory(identifier)
    mocked = mock_saltedge.create_customer(identifier)

    def check_response(response):
        assert ["data"] == list(response.keys())
        check_customer_schema(response["data"])

    check_response(actual)
    check_response(mocked)


def test_remove_customer_successfully(
    mock_saltedge, actual_saltedge, mocked_customer_1234, actual_customer_1234
):
    actual = actual_saltedge.remove_customer(actual_customer_1234["id"])
    mocked = mock_saltedge.remove_customer(mocked_customer_1234["id"])

    def check_response(response):
        assert ["data"] == list(response.keys())
        assert ["id", "deleted"] == list(response["data"].keys())

    check_response(actual)
    check_response(mocked)


def test_show_customer_successfully(
    mock_saltedge, actual_saltedge, mocked_customer_1234, actual_customer_1234
):
    actual = actual_saltedge.show_customer(actual_customer_1234["id"])
    mocked = mock_saltedge.show_customer(mocked_customer_1234["id"])

    def check_response(response):
        assert ["data"] == list(response.keys())
        check_customer_schema(response["data"])

    check_response(actual)
    check_response(mocked)


def test_list_customers_successfully(
    mock_saltedge, actual_saltedge, actual_customer_factory
):
    actual_customer_factory("test_a")
    actual_customer_factory("test_b")
    mock_saltedge.create_customer("test_a")
    mock_saltedge.create_customer("test_b")

    actual = actual_saltedge.list_customers()
    mocked = mock_saltedge.list_customers()

    def check_response(response):
        assert ["data", "meta"] == list(response.keys())
        for customer in response["data"]:
            check_customer_schema(customer)
        assert ["next_id", "next_page"] == list(response["meta"].keys())

    check_response(actual)
    check_response(mocked)


def test_create_connect_session_successfully(
    mock_saltedge, actual_saltedge, mocked_customer_1234, actual_customer_1234
):
    redirect_url = "http://www.example.com"

    actual = actual_saltedge.create_connect_session(
        actual_customer_1234["id"], redirect_url
    )
    mocked = mock_saltedge.create_connect_session(
        mocked_customer_1234["id"], redirect_url,
    )

    def check_response(response):
        assert ["data"] == list(response.keys())
        assert ["expires_at", "connect_url"] == list(response["data"].keys())

    check_response(actual)
    check_response(mocked)


def test_show_connection_successfully(
    mock_saltedge, actual_saltedge, mocked_connection_1234, predefined_connection
):
    actual = actual_saltedge.show_connection(predefined_connection["id"])
    mocked = mock_saltedge.show_connection(mocked_connection_1234["id"])

    def check_response(response):
        assert ["data"] == list(response.keys())
        check_connection_schema(response["data"])

    check_response(actual)
    check_response(mocked)


def test_list_connections_successfully(
    mock_saltedge, actual_saltedge, mocked_customer_1234, predefined_customer,
):
    mock_saltedge.create_connection(mocked_customer_1234["id"])
    mock_saltedge.create_connection(mocked_customer_1234["id"])

    actual = actual_saltedge.list_connections(predefined_customer["id"])
    mocked = mock_saltedge.list_connections(mocked_customer_1234["id"])

    def check_response(response):
        assert ["data", "meta"] == list(response.keys())
        for connection in response["data"]:
            check_connection_schema(connection)
        assert ["next_id", "next_page"] == list(response["meta"].keys())

    check_response(actual)
    check_response(mocked)


def test_list_accounts_successfully(
    mock_saltedge, actual_saltedge, mocked_connection_1234, predefined_connection
):
    mock_saltedge.create_account(mocked_connection_1234["id"])
    mock_saltedge.create_account(mocked_connection_1234["id"])

    actual = actual_saltedge.list_accounts(predefined_connection["id"])
    mocked = mock_saltedge.list_accounts(mocked_connection_1234["id"])

    def check_response(response):
        assert ["data", "meta"] == list(response.keys())
        for account in response["data"]:
            check_account_schema(account)
        assert ["next_id", "next_page"] == list(response["meta"].keys())

    check_response(actual)
    check_response(mocked)


def test_list_transactions_successfully(
    mock_saltedge,
    actual_saltedge,
    mocked_connection_1234,
    predefined_connection,
    mocked_account_1234,
    predefined_account,
):
    mock_saltedge.create_transaction(mocked_account_1234["id"])
    mock_saltedge.create_transaction(mocked_account_1234["id"])

    actual = actual_saltedge.list_transactions(
        predefined_connection["id"], predefined_account["id"]
    )
    mocked = mock_saltedge.list_transactions(
        mocked_connection_1234["id"], mocked_account_1234["id"]
    )

    def check_response(response):
        assert ["data", "meta"] == list(response.keys())
        for transaction in response["data"]:
            check_transaction_schema(transaction)
        assert ["next_id", "next_page"] == list(response["meta"].keys())

    check_response(actual)
    check_response(mocked)
