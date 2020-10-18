from typing import Any

import swagger_client as saltedge_client


def create_customer_in_saltedge(
    profile: Any, api: saltedge_client.CustomersApi
) -> None:
    data = saltedge_client.CustomerRequestBodyData(
        identifier=str(profile.user.username)
    )
    body = saltedge_client.CustomerRequestBody(data)
    response = api.customers_post(body=body)
    profile.external_id = int(response.data.id)
    profile.save()


def remove_customer_from_saltedge(
    profile: Any, api: saltedge_client.CustomersApi
) -> None:
    api.customers_customer_id_delete(str(profile.external_id))
    profile.external_id = None
    profile.save()
