from django import forms
from django.conf import settings
import os
from .saltedge import SaltEdge
from .models import Account


class ImportAccountsForm(forms.Form):
    def import_accounts(self):
        app = SaltEdge(
            os.environ["APP_ID"], os.environ["SECRET"], "accounts/private.pem"
        )
        url = "https://www.saltedge.com/api/v5/accounts?connection_id={}".format(
            os.environ["CONNECTION_ID"]
        )
        response = app.get(url)
        data = response.json()

        for imported_account in data["data"]:
            imported_id = int(imported_account["id"])

            t, created = Account.objects.update_or_create(
                external_id=imported_id,
                defaults={
                    "name": imported_account["name"],
                    "account_type": Account.AccountType.ACCOUNT,
                },
            )
