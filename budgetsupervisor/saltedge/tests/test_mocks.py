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
        customer = actual_wrapper.create_customer(identifier)["data"]
        created_ids.append(customer["id"])
        return customer

    yield create_customer

    existing_ids = [c["id"] for c in actual_wrapper.list_customers()["data"]]
    for id in created_ids:
        if id in existing_ids:
            actual_wrapper.remove_customer(id)


@pytest.fixture
def actual_customer_1234(actual_customer_factory):
    return actual_customer_factory("test_1234")


@pytest.fixture
def mocked_customer_factory(mock_wrapper):
    def create_customer(
        *args, **kwargs,
    ):
        return mock_wrapper.create_customer(*args, **kwargs)["data"]

    return create_customer


@pytest.fixture
def mocked_customer_1234(mocked_customer_factory):
    return mocked_customer_factory("test_1234")


def test_create_customer_successfully(mock_wrapper, actual_customer_factory):
    identifier = "test"
    actual = actual_customer_factory(identifier)
    mocked = mock_wrapper.create_customer(
        identifier, mock_id=actual["id"], mock_secret=actual["secret"]
    )

    assert mocked == {"data": actual}


def test_remove_customer_successfully(
    mock_wrapper, actual_wrapper, actual_customer_1234
):
    id = actual_customer_1234["id"]
    actual = actual_wrapper.remove_customer(id)
    mocked = mock_wrapper.remove_customer(id)

    assert mocked == actual


def test_list_customers_successfully(
    mock_wrapper, actual_wrapper, actual_customer_factory, mocked_customer_factory
):
    actual_customer_a = actual_customer_factory("test_a")
    mocked_customer_a = mocked_customer_factory(
        "test_a",
        mock_id=actual_customer_a["id"],
        mock_secret=actual_customer_a["secret"],
    )
    actual_customer_b = actual_customer_factory("test_b")
    mocked_customer_b = mocked_customer_factory(
        "test_b",
        mock_id=actual_customer_b["id"],
        mock_secret=actual_customer_b["secret"],
    )

    actual = actual_wrapper.list_customers()
    mocked = mock_wrapper.list_customers()

    assert actual_customer_a in actual["data"]
    assert actual_customer_b in actual["data"]
    assert "next_id" in actual["meta"]
    assert "next_page" in actual["meta"]

    assert mocked_customer_a in mocked["data"]
    assert mocked_customer_b in mocked["data"]
    assert "next_id" in mocked["meta"]
    assert "next_page" in mocked["meta"]


def test_create_connect_session_successfully(
    mock_wrapper, actual_wrapper, mocked_customer_1234, actual_customer_1234
):
    redirect_url = "https://www.google.com"

    actual = actual_wrapper.create_connect_session(
        actual_customer_1234["id"], redirect_url
    )
    mocked = mock_wrapper.create_connect_session(
        mocked_customer_1234["id"],
        redirect_url,
        mock_expiration=actual["data"]["expires_at"],
        mock_url=actual["data"]["connect_url"],
    )

    assert mocked == actual
