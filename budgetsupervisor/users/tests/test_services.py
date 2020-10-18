from typing import Callable

import swagger_client as saltedge_client
from users.models import Profile
from users.services import create_customer_in_saltedge, remove_customer_from_saltedge


def test_create_customer_in_saltedge(
    profile_foo: Profile,
    customers_api: saltedge_client.CustomersApi,
    saltedge_customer_factory: Callable[..., saltedge_client.Customer],
) -> None:
    data = saltedge_customer_factory(id="123")
    customers_api.customers_post.return_value = saltedge_client.CreatedCustomerResponse(
        data=data
    )

    assert profile_foo.external_id is None
    create_customer_in_saltedge(profile_foo, customers_api)
    assert profile_foo.external_id == 123


def test_remove_customer_from_saltedge(
    profile_foo_external: Profile, customers_api: saltedge_client.CustomersApi
) -> None:
    data = saltedge_client.RemovedCustomerResponseData(
        deleted=True, id=str(profile_foo_external.external_id)
    )
    customers_api.customers_customer_id_delete.return_value = saltedge_client.RemovedCustomerResponse(
        data=data
    )

    assert profile_foo_external.external_id is not None
    remove_customer_from_saltedge(profile_foo_external, customers_api)
    assert profile_foo_external.external_id is None
