from django import forms
from .models import Account, Connection


class ImportAccountsForm(forms.Form):
    connection = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["connection"].queryset = Connection.objects.filter(user=user)


class ImportTransactionsForm(forms.Form):
    account = forms.ModelChoiceField(queryset=None)

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
    accounts = forms.ModelMultipleChoiceField(queryset=None)
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
