from django import forms
from django.conf import settings
from django.utils.dateparse import parse_datetime
import os
import json
from saltedge.saltedge import SaltEdge
from .models import Account, Category, Connection, Transaction
from decimal import Decimal
from django.shortcuts import redirect


class ImportAccountsForm(forms.Form):
    def import_accounts(self):
        app = SaltEdge(
            os.environ["APP_ID"], os.environ["SECRET"], "saltedge/private.pem"
        )
        url = "https://www.saltedge.com/api/v5/accounts?connection_id={}".format(
            os.environ["CONNECTION_ID"]
        )
        response = app.get(url)
        data = response.json()

        for imported_account in data["data"]:
            imported_id = int(imported_account["id"])

            a, created = Account.objects.update_or_create(
                external_id=imported_id,
                defaults={
                    "name": imported_account["name"],
                    "account_type": Account.AccountType.ACCOUNT,
                },
            )


class ImportTransactionsForm(forms.Form):
    def import_transactions(self, account_id):
        app = SaltEdge(
            os.environ["APP_ID"], os.environ["SECRET"], "saltedge/private.pem"
        )
        url = "https://www.saltedge.com/api/v5/transactions?connection_id={}&account_id={}".format(
            os.environ["CONNECTION_ID"], account_id
        )
        response = app.get(url)
        data = response.json()

        uncategorized = Category.objects.get(name="Uncategorized")

        for imported_transaction in data["data"]:
            imported_id = int(imported_transaction["id"])

            escaped_category = imported_transaction["category"].replace("_", " ")
            category = Category.objects.filter(name__iexact=escaped_category)
            category = category[0] if category else uncategorized

            t, created = Transaction.objects.update_or_create(
                external_id=imported_id,
                defaults={
                    "date": imported_transaction["made_on"],
                    "amount": imported_transaction["amount"],
                    "payee": "",
                    "category": category,
                    "description": imported_transaction["description"],
                    "account_id": Account.objects.get(
                        external_id=imported_transaction["account_id"]
                    ).id,
                },
            )


class CreateConnectionForm(forms.Form):
    def create_connection(self, redirect_url):
        app = SaltEdge(
            os.environ["APP_ID"], os.environ["SECRET"], "saltedge/private.pem"
        )
        url = "https://www.saltedge.com/api/v5/connect_sessions/create"
        payload = json.dumps(
            {
                "data": {
                    "customer_id": str(os.environ["CUSTOMER_ID"]),
                    "consent": {"scopes": ["account_details", "transactions_details"]},
                    "attempt": {"return_to": redirect_url},
                }
            }
        )
        response = app.post(url, payload)
        data = response.json()

        return redirect(data["data"]["connect_url"])


class ImportConnectionsForm(forms.Form):
    def import_connections(self):
        app = SaltEdge(
            os.environ["APP_ID"], os.environ["SECRET"], "saltedge/private.pem"
        )
        url = "https://www.saltedge.com/api/v5/connections?customer_id={}".format(
            os.environ["CUSTOMER_ID"]
        )
        response = app.get(url)
        data = response.json()

        for imported_connection in data["data"]:
            imported_id = int(imported_connection["id"])

            c, created = Connection.objects.update_or_create(
                external_id=imported_id,
                defaults={"provider": imported_connection["provider_name"]},
            )
