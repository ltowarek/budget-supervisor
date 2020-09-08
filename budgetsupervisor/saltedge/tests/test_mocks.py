from .mocks import MockSaltEdgeWrapper
from ..wrapper import SaltEdgeWrapper
import os
import pytest


@pytest.fixture
def actual_wrapper_factory():
    def create_wrapper(app_id, secret, private_path):
        return SaltEdgeWrapper(app_id, secret, private_path)

    return create_wrapper


@pytest.fixture
def actual_wrapper(actual_wrapper_factory):
    app_id = os.environ["APP_ID"]
    secret = os.environ["SECRET"]
    private_path = "saltedge/private.pem"
    return actual_wrapper_factory(app_id, secret, private_path)


@pytest.fixture
def mock_wrapper_factory():
    def create_wrapper(app_id, secret, private_path):
        return MockSaltEdgeWrapper(app_id, secret, private_path)

    return create_wrapper


@pytest.fixture
def mock_wrapper(mock_wrapper_factory):
    app_id = os.environ["APP_ID"]
    secret = os.environ["SECRET"]
    private_path = "saltedge/private.pem"
    return mock_wrapper_factory(app_id, secret, private_path)


@pytest.fixture
def actual_customer_factory(actual_wrapper):
    created_ids = []

    def create_customer(identifier):
        response = actual_wrapper.create_customer(identifier)
        customer = response["data"]
        created_ids.append(customer["id"])
        return response

    yield create_customer

    existing_ids = [c["id"] for c in actual_wrapper.list_customers()["data"]]
    for id in created_ids:
        if id in existing_ids:
            actual_wrapper.remove_customer(id)


@pytest.fixture
def actual_customer_1234(actual_customer_factory):
    return actual_customer_factory("test_1234")["data"]


@pytest.fixture
def mocked_customer_factory(mock_wrapper):
    def create_customer(
        *args, **kwargs,
    ):
        return mock_wrapper.create_customer(*args, **kwargs)

    return create_customer


@pytest.fixture
def mocked_customer_1234(mocked_customer_factory):
    return mocked_customer_factory("test_1234")["data"]


@pytest.fixture
def predefined_customer(actual_wrapper):
    return actual_wrapper.show_customer(os.environ["CUSTOMER_ID"])["data"]


@pytest.fixture
def predefined_connection(actual_wrapper):
    return actual_wrapper.show_connection(os.environ["CONNECTION_ID"])["data"]


@pytest.fixture
def mocked_connection_factory(mock_wrapper):
    def create_connection(
        *args, **kwargs,
    ):
        return mock_wrapper.create_connection(*args, **kwargs)

    return create_connection


@pytest.fixture
def mocked_connection_1234(mocked_connection_factory, mocked_customer_1234):
    return mocked_connection_factory(mocked_customer_1234["id"])["data"]


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


def test_create_customer_successfully(mock_wrapper, actual_customer_factory):
    identifier = "test"
    actual = actual_customer_factory(identifier)
    mocked = mock_wrapper.create_customer(identifier)

    def check_response(response):
        assert ["data"] == list(response.keys())
        check_customer_schema(response["data"])

    check_response(actual)
    check_response(mocked)


def test_remove_customer_successfully(
    mock_wrapper, actual_wrapper, mocked_customer_1234, actual_customer_1234
):
    actual = actual_wrapper.remove_customer(actual_customer_1234["id"])
    mocked = mock_wrapper.remove_customer(mocked_customer_1234["id"])

    def check_response(response):
        assert ["data"] == list(response.keys())
        assert ["id", "deleted"] == list(response["data"].keys())

    check_response(actual)
    check_response(mocked)


def test_show_customer_successfully(
    mock_wrapper, actual_wrapper, mocked_customer_1234, actual_customer_1234
):
    actual = actual_wrapper.show_customer(actual_customer_1234["id"])
    mocked = mock_wrapper.show_customer(mocked_customer_1234["id"])

    def check_response(response):
        assert ["data"] == list(response.keys())
        check_customer_schema(response["data"])

    check_response(actual)
    check_response(mocked)


def test_list_customers_successfully(
    mock_wrapper, actual_wrapper, mocked_customer_factory, actual_customer_factory
):
    actual_customer_factory("test_a")
    actual_customer_factory("test_b")
    mocked_customer_factory("test_a")
    mocked_customer_factory("test_b")

    actual = actual_wrapper.list_customers()
    mocked = mock_wrapper.list_customers()

    def check_response(response):
        assert ["data", "meta"] == list(response.keys())
        for customer in response["data"]:
            check_customer_schema(customer)
        assert ["next_id", "next_page"] == list(response["meta"].keys())

    check_response(actual)
    check_response(mocked)


def test_create_connect_session_successfully(
    mock_wrapper, actual_wrapper, mocked_customer_1234, actual_customer_1234
):
    redirect_url = "http://www.example.com"

    actual = actual_wrapper.create_connect_session(
        actual_customer_1234["id"], redirect_url
    )
    mocked = mock_wrapper.create_connect_session(
        mocked_customer_1234["id"], redirect_url,
    )

    def check_response(response):
        assert ["data"] == list(response.keys())
        assert ["expires_at", "connect_url"] == list(response["data"].keys())

    check_response(actual)
    check_response(mocked)


def test_show_connection_successfully(
    mock_wrapper, actual_wrapper, mocked_connection_1234, predefined_connection
):
    actual = actual_wrapper.show_connection(predefined_connection["id"])
    mocked = mock_wrapper.show_connection(mocked_connection_1234["id"])

    def check_response(response):
        assert ["data"] == list(response.keys())
        check_connection_schema(response["data"])

    check_response(actual)
    check_response(mocked)


def test_list_connections_successfully(
    mock_wrapper,
    actual_wrapper,
    mocked_customer_1234,
    predefined_customer,
    mocked_connection_factory,
):
    mocked_connection_factory(mocked_customer_1234["id"])
    mocked_connection_factory(mocked_customer_1234["id"])

    actual = actual_wrapper.list_connections(predefined_customer["id"])
    mocked = mock_wrapper.list_connections(mocked_customer_1234["id"])

    def check_response(response):
        assert ["data", "meta"] == list(response.keys())
        for connection in response["data"]:
            check_connection_schema(connection)
        assert ["next_id", "next_page"] == list(response["meta"].keys())

    check_response(actual)
    check_response(mocked)
