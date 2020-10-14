from typing import Any

from budget.models import Account, Connection, Transaction


def disconnect_accounts_and_transactions(
    sender: Connection, instance: Connection, **kwargs: Any
) -> None:
    accounts = Account.objects.filter(connection=instance)
    accounts.update(external_id=None)
    for account in accounts:
        transactions = Transaction.objects.filter(account=account)
        transactions.update(external_id=None)
