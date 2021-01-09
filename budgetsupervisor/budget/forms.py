from typing import Any

from django import forms
from django.conf import settings

from .models import Account, Transaction

date_input_with_placeholder = forms.DateInput(
    attrs={"placeholder": settings.DATE_INPUT_FORMATS[0].replace("%", "")}
)


class CreateConnectionForm(forms.Form):
    pass


class RefreshConnectionForm(forms.Form):
    pass


class UpdateAccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ["name", "alias", "account_type"]

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        if self.instance.external_id:
            self.fields["name"].disabled = True
            self.fields["alias"].disabled = True
            self.fields["account_type"].disabled = True


class CreateTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["date", "amount", "payee", "category", "description", "account"]
        localized_fields = "__all__"
        widgets = {"date": date_input_with_placeholder}


class UpdateTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["date", "amount", "payee", "category", "description", "account"]
        localized_fields = "__all__"
        widgets = {"date": date_input_with_placeholder}

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        if self.instance.external_id:
            self.fields["date"].disabled = True
            self.fields["amount"].disabled = True
            self.fields["description"].disabled = True
            self.fields["account"].disabled = True


class ReportBalanceForm(forms.Form):
    accounts = forms.ModelMultipleChoiceField(queryset=None)
    from_date = forms.DateField(
        required=False, widget=date_input_with_placeholder, localize=True
    )
    to_date = forms.DateField(
        required=False, widget=date_input_with_placeholder, localize=True
    )

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
