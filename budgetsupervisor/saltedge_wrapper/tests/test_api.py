import swagger_client as saltedge_client
import pytest
from saltedge_wrapper.factory import (
    customers_api,
    connect_sessions_api,
    connections_api,
    accounts_api,
    transactions_api,
)


pytestmark = pytest.mark.saltedge


@pytest.fixture
def customer_factory():
    created_ids = []

    def create_customer(**kwargs):
        data = saltedge_client.CustomerRequestBodyData(**kwargs)
        body = saltedge_client.CustomerRequestBody(data)
        customer = customers_api().customers_post(body=body).data
        created_ids.append(customer.id)
        return customer

    yield create_customer

    existing_ids = [c.id for c in customers_api().customers_get().data]
    for id in created_ids:
        if id in existing_ids:
            customers_api().customers_customer_id_delete(id)


@pytest.fixture
def customer_1234(customer_factory):
    return customer_factory(identifier="test_1234")


def test_create_customer_successfully(customer_factory):
    identifier = "test"
    customer = customer_factory(identifier=identifier)
    assert customer.identifier == identifier


def test_remove_customer_successfully(customer_1234):
    response = customers_api().customers_customer_id_delete(customer_1234.id)
    assert response.data.deleted is True


def test_show_customer_successfully(customer_1234):
    response = customers_api().customers_customer_id_get(customer_1234.id)
    assert response.data == customer_1234


def test_list_customers_successfully(customer_factory):
    customer_a = customer_factory(identifier="test_a")
    customer_b = customer_factory(identifier="test_b")
    response = customers_api().customers_get()
    assert customer_a in response.data
    assert customer_b in response.data


def test_create_connect_session_successfully(predefined_customer):
    return_to = "http://www.example.com"
    attempt = saltedge_client.AttemptRequestBody(
        return_to=return_to, store_credentials=False
    )
    consent = saltedge_client.ConsentRequestBody(
        scopes=["account_details", "transactions_details"]
    )
    data = saltedge_client.ConnectSessionRequestBodyData(
        predefined_customer.id, consent, attempt=attempt
    )
    body = saltedge_client.ConnectSessionRequestBody(data)
    response = connect_sessions_api().connect_sessions_create_post(body=body)
    assert "https://www.saltedge.com/connect?token=" in response.data.connect_url


def test_show_connection_successfully(predefined_connection):
    response = connections_api().connections_connection_id_get(predefined_connection.id)
    assert response.data == predefined_connection


def test_list_connections_successfully(
    predefined_connection, predefined_customer,
):
    response = connections_api().connections_get(predefined_customer.id)
    assert predefined_connection in response.data


def test_list_accounts_successfully(
    predefined_connection, predefined_customer, predefined_account
):
    response = accounts_api().accounts_get(
        predefined_connection.id, customer_id=predefined_customer.id
    )
    assert predefined_account in response.data


def test_list_transactions_successfully(predefined_connection, predefined_account):
    response = transactions_api().transactions_get(
        predefined_connection.id, account_id=predefined_account.id
    )
    assert len(response.data) > 0


def test_transaction_categories_lowercase(predefined_connection, predefined_account):
    response = transactions_api().transactions_get(
        predefined_connection.id, account_id=predefined_account.id
    )
    for transaction in response.data:
        assert transaction.category == transaction.category.lower()


def test_transaction_categories_no_spaces(predefined_connection, predefined_account):
    response = transactions_api().transactions_get(
        predefined_connection.id, account_id=predefined_account.id
    )
    for transaction in response.data:
        assert transaction.category.count(" ") == 0
