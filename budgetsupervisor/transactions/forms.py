from django import forms
from django.conf import settings
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

        transactions = []
        for imported_transaction in data['data']:
            t = Transaction()
            t.date = imported_transaction['made_on']
            t.amount = imported_transaction['amount']
            t.payee = ""
            t.category = Category.objects.get(name="Uncategorized")
            transactions.append(t)
        Transaction.objects.bulk_create(transactions)
