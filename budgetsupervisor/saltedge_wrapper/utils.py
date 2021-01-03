from typing import List

import swagger_client as saltedge_client


def create_connect_session(
    redirect_url: str,
    customer_id: str,
    connect_sessions_api: saltedge_client.ConnectSessionsApi,
) -> str:
    consent = saltedge_client.ConsentRequestBody(
        scopes=["account_details", "transactions_details"]
    )
    attempt = saltedge_client.AttemptRequestBody(
        return_to=redirect_url, store_credentials=False
    )
    data = saltedge_client.ConnectSessionRequestBodyData(
        customer_id=customer_id,
        consent=consent,
        attempt=attempt,
        categorization="none",
    )
    body = saltedge_client.ConnectSessionRequestBody(data)
    response = connect_sessions_api.connect_sessions_create_post(body=body)
    return response.data.connect_url


def get_connection(
    connection_id: str, connections_api: saltedge_client.ConnectionsApi,
) -> saltedge_client.Connection:
    response = connections_api.connections_connection_id_get(connection_id)
    return response.data


def get_connections(
    customer_id: str, connections_api: saltedge_client.ConnectionsApi,
) -> List[saltedge_client.Connection]:
    connections = []
    from_id = None
    while True:
        response = connections_api.connections_get(customer_id, from_id=from_id)
        connections.extend(response.data)
        if not response.meta or not response.meta.next_id:
            break
        from_id = response.meta.next_id
    return connections


def refresh_connection_in_saltedge(
    redirect_url: str,
    connection_id: str,
    connect_sessions_api: saltedge_client.ConnectSessionsApi,
) -> str:
    attempt = saltedge_client.AttemptRequestBody(
        return_to=redirect_url, store_credentials=False
    )
    data = saltedge_client.RefreshSessionRequestBodyData(
        connection_id=connection_id, attempt=attempt, categorization="none",
    )
    body = saltedge_client.RefreshSessionRequestBody(data)
    response = connect_sessions_api.connect_sessions_refresh_post(body=body)
    return response.data.connect_url


def remove_connection_from_saltedge(
    connection_id: str, connections_api: saltedge_client.ConnectionsApi
) -> None:
    connections_api.connections_connection_id_delete(connection_id)


def get_accounts(
    connection_id: str, accounts_api: saltedge_client.AccountsApi,
) -> List[saltedge_client.Account]:
    accounts = []
    from_id = None
    while True:
        response = accounts_api.accounts_get(connection_id, from_id=from_id)
        accounts.extend(response.data)
        if not response.meta or not response.meta.next_id:
            break
        from_id = response.meta.next_id
    return accounts


def get_transactions(
    connection_id: str,
    account_id: str,
    transactions_api: saltedge_client.TransactionsApi,
) -> List[saltedge_client.Transaction]:
    transactions = []
    from_id = None
    while True:
        response = transactions_api.transactions_get(
            connection_id=connection_id, account_id=account_id, from_id=from_id,
        )
        transactions.extend(response.data)
        if not response.meta or not response.meta.next_id:
            break
        from_id = response.meta.next_id
    return transactions


def get_pending_transactions(
    connection_id: str,
    account_id: str,
    transactions_api: saltedge_client.TransactionsApi,
) -> List[saltedge_client.Transaction]:
    transactions = []
    from_id = None
    while True:
        response = transactions_api.transactions_pending_get(
            connection_id=connection_id, account_id=account_id, from_id=from_id,
        )
        transactions.extend(response.data)
        if not response.meta or not response.meta.next_id:
            break
        from_id = response.meta.next_id
    return transactions
