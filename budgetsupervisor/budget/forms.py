from typing import Any

from django import forms

from .models import Account


class CreateConnectionForm(forms.Form):
    pass


class RefreshConnectionForm(forms.Form):
    pass


class ReportBalanceForm(forms.Form):
    accounts = forms.ModelMultipleChoiceField(queryset=None)
    from_date = forms.DateField(required=False)
    to_date = forms.DateField(required=False)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["accounts"].queryset = Account.objects.filter(user=user)

    def clean(self) -> None:
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date and to_date < from_date:
            self.add_error("to_date", "To date can't point before from date.")
