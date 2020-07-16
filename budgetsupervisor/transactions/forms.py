from django import forms
from django.conf import settings
from django.utils.dateparse import parse_datetime
import os
from .saltedge import SaltEdge
from .models import Transaction, Category
from decimal import Decimal


class ImportTransactionsForm(forms.Form):
    def import_transactions(self):
        app = SaltEdge(os.environ["APP_ID"], os.environ["SECRET"], "transactions/private.pem")
        url = "https://www.saltedge.com/api/v5/transactions?connection_id={}&account_id={}".format(os.environ["CONNECTION_ID"], os.environ["ACCOUNT_ID"])
        response = app.get(url)
        data = response.json()

        already_imported_ids = Transaction.objects.filter(external_id__isnull=False).values_list("external_id", flat=True)

        for imported_transaction in data['data']:
            imported_id = int(imported_transaction['id'])

            if imported_id in already_imported_ids:
                continue

            escaped_category = imported_transaction["category"].replace("_", " ")
            category = Category.objects.filter(name__iexact=escaped_category)
            category = category[0] if category else Category.objects.get(name="Uncategorized")

            t, created = Transaction.objects.update_or_create(
                external_id=imported_id,
                defaults={
                    "date": imported_transaction['made_on'],
                    "amount": imported_transaction['amount'],
                    "payee": "",
                    "category": category,
                    "description": imported_transaction['description'],
                }
            )
