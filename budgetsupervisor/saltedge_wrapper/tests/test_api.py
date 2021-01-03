from typing import Any, Callable, Iterable

import pytest
import swagger_client as saltedge_client
from saltedge_wrapper.factory import customers_api

pytestmark = pytest.mark.saltedge


@pytest.fixture
def customer_factory() -> Iterable[Callable[..., saltedge_client.Customer]]:
    created_ids = []

    def create_customer(**kwargs: Any) -> saltedge_client.Customer:
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
def customer_1234(
    customer_factory: Callable[..., saltedge_client.Customer]
) -> saltedge_client.Customer:
    return customer_factory(identifier="test_1234")


def test_create_customer_successfully(
    customer_factory: Callable[..., saltedge_client.Customer]
) -> None:
    identifier = "test"
    customer = customer_factory(identifier=identifier)
    assert customer.identifier == identifier


def test_remove_customer_successfully(customer_1234: saltedge_client.Customer) -> None:
    response = customers_api().customers_customer_id_delete(customer_1234.id)
    assert response.data.deleted is True


def test_show_customer_successfully(customer_1234: saltedge_client.Customer) -> None:
    response = customers_api().customers_customer_id_get(customer_1234.id)
    assert response.data == customer_1234


def test_list_customers_successfully(
    customer_factory: Callable[..., saltedge_client.Customer]
) -> None:
    customer_a = customer_factory(identifier="test_a")
    customer_b = customer_factory(identifier="test_b")
    response = customers_api().customers_get()
    assert customer_a in response.data
    assert customer_b in response.data
