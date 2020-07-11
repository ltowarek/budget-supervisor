from django import forms
from django.conf import settings
import os
from .saltedge import SaltEdge
from .models import Transaction, Category, Payee
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
            amount = Decimal(imported_transaction['amount'])
            t.amount = abs(amount)
            t.transaction_type = Transaction.TransactionType.DEPOSIT if amount >= 0 else Transaction.TransactionType.WITHDRAWAL
            t.payee = Payee.objects.get(id=1) #TMP
            t.category = Category.objects.get(id=1) #TMP
            transactions.append(t)
        Transaction.objects.bulk_create(transactions)
