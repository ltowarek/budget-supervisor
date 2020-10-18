import datetime
from typing import Dict, List

import swagger_client as saltedge_client
from budget.models import Account, Connection, Transaction
from django.db.models import Sum
from users.models import User


def create_connection_in_saltedge(
    redirect_url: str,
    customer_id: int,
    connect_sessions_api: saltedge_client.ConnectSessionsApi,
) -> str:
    attempt = saltedge_client.AttemptRequestBody(
        return_to=redirect_url, store_credentials=False
    )
    consent = saltedge_client.ConsentRequestBody(
        scopes=["account_details", "transactions_details"]
    )
    data = saltedge_client.ConnectSessionRequestBodyData(
        str(customer_id), consent, attempt=attempt
    )
    body = saltedge_client.ConnectSessionRequestBody(data)
    response = connect_sessions_api.connect_sessions_create_post(body=body)
    return response.data.connect_url


def import_connections_from_saltedge(
    user: User, customer_id: int, connections_api: saltedge_client.ConnectionsApi,
) -> List[Connection]:
    response = connections_api.connections_get(str(customer_id))
    new_connections = []
    for imported_connection in response.data:
        imported_id = int(imported_connection.id)

        c, created = Connection.objects.update_or_create(
            external_id=imported_id,
            defaults={"provider": imported_connection.provider_name, "user": user},
        )
        if created:
            new_connections.append(c)
    return new_connections


def remove_connection_from_saltedge(
    connection: Connection, connections_api: saltedge_client.ConnectionsApi
) -> None:
    connections_api.connections_connection_id_delete(str(connection.external_id))


def import_accounts_from_saltedge(
    user: User, connection_id: int, accounts_api: saltedge_client.AccountsApi
) -> List["Account"]:
    response = accounts_api.accounts_get(str(connection_id))
    new_accounts = []
    for imported_account in response.data:
        imported_id = int(imported_account.id)

        a, created = Account.objects.update_or_create(
            external_id=imported_id,
            defaults={
                "name": imported_account.name,
                "account_type": Account.AccountType.ACCOUNT,
                "connection": Connection.objects.get(external_id=connection_id),
                "user": user,
            },
        )
        if created:
            new_accounts.append(a)
    return new_accounts


def import_transactions_from_saltedge(
    user: User,
    connection_id: int,
    account_id: int,
    transactions_api: saltedge_client.TransactionsApi,
) -> List[Transaction]:
    response = transactions_api.transactions_get(
        str(connection_id), account_id=str(account_id)
    )
    new_transactions = []
    for imported_transaction in response.data:
        imported_id = int(imported_transaction.id)

        t, created = Transaction.objects.update_or_create(
            external_id=imported_id,
            defaults={
                "date": imported_transaction.made_on,
                "amount": imported_transaction.amount,
                "payee": "",
                "category": None,
                "description": imported_transaction.description,
                "account_id": Account.objects.get(
                    external_id=imported_transaction.account_id
                ).id,
                "user": user,
            },
        )
        if created:
            new_transactions.append(t)
    return new_transactions


def get_category_balance(
    accounts: List[Account],
    user: User,
    from_date: datetime.date = None,
    to_date: datetime.date = None,
) -> Dict[str, float]:
    q = {"account__in": accounts, "user": user}
    if from_date:
        q["date__gte"] = from_date
    if to_date:
        q["date__lte"] = to_date

    queryset = (
        Transaction.objects.filter(**q).values("category__name").annotate(Sum("amount"))
    )
    balance = {d["category__name"]: d["amount__sum"] for d in queryset}
    balance["Total"] = sum(balance.values())
    return balance
