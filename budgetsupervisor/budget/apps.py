from django.apps import AppConfig
from django.db.models.signals import pre_delete


class BudgetConfig(AppConfig):
    name = "budget"

    def ready(self) -> None:
        from budget.models import Connection
        from budget.signals import disconnect_accounts_and_transactions

        pre_delete.connect(disconnect_accounts_and_transactions, sender=Connection)
