import os

import swagger_client as saltedge_client


def api_configuration() -> saltedge_client.Configuration:
    configuration = saltedge_client.Configuration()
    configuration.api_key["App-id"] = os.environ["SALTEDGE_APP_ID"]
    configuration.api_key["Secret"] = os.environ["SALTEDGE_SECRET"]
    return configuration


def api_client() -> saltedge_client.CustomersApi:
    return saltedge_client.ApiClient(api_configuration())


def customers_api() -> saltedge_client.CustomersApi:
    return saltedge_client.CustomersApi(api_client())


def connect_sessions_api() -> saltedge_client.ConnectSessionsApi:
    return saltedge_client.ConnectSessionsApi(api_client())


def connections_api() -> saltedge_client.ConnectionsApi:
    return saltedge_client.ConnectionsApi(api_client())


def accounts_api() -> saltedge_client.AccountsApi:
    return saltedge_client.AccountsApi(api_client())


def transactions_api() -> saltedge_client.TransactionsApi:
    return saltedge_client.TransactionsApi(api_client())
