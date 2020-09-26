from django import forms
from django.conf import settings
from django.utils.dateparse import parse_datetime
import os
import json
from .models import Account, Category, Connection, Transaction
from decimal import Decimal
from django.shortcuts import redirect
from .models import Account, Connection
from django.contrib.auth.models import User


class ConnectionModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.provider


class AccountModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class AccountModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class ImportAccountsForm(forms.Form):
    connection = ConnectionModelChoiceField(Connection.objects.none())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["connection"].queryset = Connection.objects.filter(user=user)


class ImportTransactionsForm(forms.Form):
    account = AccountModelChoiceField(Account.objects.all())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["account"].queryset = Account.objects.filter(
            user=user, external_id__isnull=False
        )


class CreateConnectionForm(forms.Form):
    pass


class ImportConnectionsForm(forms.Form):
    pass


class ReportBalanceForm(forms.Form):
    accounts = AccountModelMultipleChoiceField(Account.objects.none())
    from_date = forms.DateField(required=False)
    to_date = forms.DateField(required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["accounts"].queryset = Account.objects.filter(user=user)

    def clean(self):
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date and to_date < from_date:
            self.add_error("to_date", "To date can't point before from date.")
