import datetime
from typing import Dict, List, Optional, Tuple

import swagger_client as saltedge_client
from budget.models import Account, Connection, Transaction
from django.db.models import Sum
from users.models import User


def import_saltedge_connection(
    saltedge_connection: saltedge_client.Connection, user: User
) -> Tuple[Connection, bool]:
    return Connection.objects.update_or_create(
        external_id=int(saltedge_connection.id),
        defaults={"provider": saltedge_connection.provider_name, "user": user},
    )


def import_saltedge_connections(
    saltedge_connections: List[saltedge_client.Connection], user: User
) -> List[Tuple["Connection", bool]]:
    output = []
    for saltedge_connection in saltedge_connections:
        output.append(import_saltedge_connection(saltedge_connection, user))
    return output


def import_saltedge_accounts(
    saltedge_accounts: List[saltedge_client.Account], user: User
) -> List[Tuple["Account", bool]]:
    output = []
    for saltedge_account in saltedge_accounts:
        o = Account.objects.update_or_create(
            external_id=int(saltedge_account.id),
            defaults={
                "name": saltedge_account.name,
                "connection": Connection.objects.get(
                    external_id=int(saltedge_account.connection_id)
                ),
                "user": user,
            },
        )
        output.append(o)
    return output


def import_saltedge_transactions(
    saltedge_transactions: List[saltedge_client.Transaction], user: User
) -> List[Tuple["Transaction", bool]]:
    output = []
    for saltedge_transaction in saltedge_transactions:
        o = Transaction.objects.update_or_create(
            external_id=int(saltedge_transaction.id),
            defaults={
                "date": saltedge_transaction.made_on,
                "amount": saltedge_transaction.amount,
                "description": saltedge_transaction.description,
                "account": Account.objects.get(
                    external_id=saltedge_transaction.account_id
                ),
                "user": user,
            },
        )
        output.append(o)
    return output


def create_initial_balance(
    account: Account,
    saltedge_account: saltedge_client.Account,
    saltedge_transactions: List[saltedge_client.Transaction],
) -> Transaction:
    initial_balance = saltedge_account.balance - sum_saltedge_transactions(
        saltedge_transactions
    )
    oldest_saltedge_transaction = get_oldest_saltedge_transaction(saltedge_transactions)
    made_on = (
        oldest_saltedge_transaction.made_on
        if oldest_saltedge_transaction
        else datetime.date.today()
    )
    return Transaction.objects.create(
        date=made_on,
        amount=initial_balance,
        description="Initial balance",
        account=account,
        user=account.user,
    )


def sum_saltedge_transactions(transactions: List[saltedge_client.Transaction]) -> float:
    return sum(t.amount for t in transactions)


def get_oldest_saltedge_transaction(
    transactions: List[saltedge_client.Transaction],
) -> Optional[saltedge_client.Transaction]:
    oldest = None
    for transaction in transactions:
        if not oldest or transaction.made_on < oldest.made_on:
            oldest = transaction
    return oldest


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
