import datetime
from typing import Any

from django import forms
from django.conf import settings
from django.db.models import Case, When

from .models import Account, Category, Connection, Transaction

date_input_with_placeholder = forms.DateInput(
    attrs={"placeholder": settings.DATE_INPUT_FORMATS[0].replace("%", "")}
)


class CreateConnectionForm(forms.Form):
    from_date = forms.DateField(
        widget=date_input_with_placeholder, localize=True, required=False
    )
    to_date = forms.DateField(
        widget=date_input_with_placeholder, localize=True, required=False
    )

    def clean(self) -> None:
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and from_date < (
            datetime.date.today() - datetime.timedelta(days=365)
        ):
            self.add_error(
                "from_date", "From date must be within exactly 365 days ago."
            )
        if from_date and from_date > datetime.date.today():
            self.add_error("from_date", "From date can't be in future.")
        if to_date and to_date < datetime.date.today():
            self.add_error("to_date", "To date can't be in past.")
        if from_date and to_date and to_date < from_date:
            self.add_error("to_date", "To date can't point before from date.")


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


class FilterAccountsForm(forms.Form):
    name = forms.CharField(required=False)
    alias = forms.CharField(required=False)
    account_types = forms.MultipleChoiceField(
        choices=Account.AccountType.choices, required=False
    )
    connections = forms.ModelMultipleChoiceField(queryset=None, required=False)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["connections"].queryset = Connection.objects.filter(
            user=user
        ).order_by("provider")


class CreateTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["date", "amount", "payee", "category", "description", "account"]
        localized_fields = "__all__"
        widgets = {"date": date_input_with_placeholder}

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["account"].queryset = Account.objects.filter(user=user).order_by(
            Case(When(alias="", then="name"), default="alias")
        )
        self.fields["category"].queryset = Category.objects.filter(user=user).order_by(
            "name"
        )


class UpdateTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["date", "amount", "payee", "category", "description", "account"]
        localized_fields = "__all__"
        widgets = {"date": date_input_with_placeholder}

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        user = self.instance.user
        self.fields["account"].queryset = Account.objects.filter(user=user).order_by(
            Case(When(alias="", then="name"), default="alias")
        )
        self.fields["category"].queryset = Category.objects.filter(user=user).order_by(
            "name"
        )
        if self.instance.external_id:
            self.fields["date"].disabled = True
            self.fields["amount"].disabled = True
            self.fields["description"].disabled = True
            self.fields["account"].disabled = True


class FilterTransactionsForm(forms.Form):
    from_date = forms.DateField(
        widget=date_input_with_placeholder, localize=True, required=False
    )
    to_date = forms.DateField(
        widget=date_input_with_placeholder, localize=True, required=False
    )
    min_amount = forms.DecimalField(required=False)
    max_amount = forms.DecimalField(required=False)
    categories = forms.ModelMultipleChoiceField(queryset=None, required=False)
    description = forms.CharField(required=False)
    accounts = forms.ModelMultipleChoiceField(queryset=None, required=False)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["categories"].queryset = Category.objects.filter(
            user=user
        ).order_by("name")
        self.fields["accounts"].queryset = Account.objects.filter(user=user).order_by(
            Case(When(alias="", then="name"), default="alias")
        )

    def clean(self) -> None:
        cleaned_data = super().clean()

        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")
        if from_date and to_date and to_date < from_date:
            self.add_error("to_date", "To date can't point before from date.")

        min_amount = cleaned_data.get("min_amount")
        max_amount = cleaned_data.get("max_amount")
        if min_amount and max_amount and max_amount < min_amount:
            self.add_error("max_amount", "Max amount can't be smaller than min amount.")


class ReportIncomeForm(forms.Form):
    accounts = forms.ModelMultipleChoiceField(queryset=None)
    from_date = forms.DateField(widget=date_input_with_placeholder, localize=True)
    to_date = forms.DateField(widget=date_input_with_placeholder, localize=True)
    excluded_categories = forms.ModelMultipleChoiceField(required=False, queryset=None)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["accounts"].queryset = Account.objects.filter(user=user).order_by(
            Case(When(alias="", then="name"), default="alias")
        )
        # TODO: Add Uncategorized/None option
        self.fields["excluded_categories"].queryset = Category.objects.filter(
            user=user
        ).order_by("name")

    def clean(self) -> None:
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date and to_date < from_date:
            self.add_error("to_date", "To date can't point before from date.")


class ReportBalanceForm(forms.Form):
    accounts = forms.ModelMultipleChoiceField(queryset=None)
    from_date = forms.DateField(widget=date_input_with_placeholder, localize=True)
    to_date = forms.DateField(widget=date_input_with_placeholder, localize=True)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["accounts"].queryset = Account.objects.filter(user=user).order_by(
            Case(When(alias="", then="name"), default="alias")
        )

    def clean(self) -> None:
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date and to_date < from_date:
            self.add_error("to_date", "To date can't point before from date.")


class ReportCategoryBalanceForm(forms.Form):
    categories = forms.ModelMultipleChoiceField(queryset=None)
    accounts = forms.ModelMultipleChoiceField(queryset=None)
    from_date = forms.DateField(widget=date_input_with_placeholder, localize=True)
    to_date = forms.DateField(widget=date_input_with_placeholder, localize=True)

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)
        self.fields["categories"].queryset = Category.objects.filter(
            user=user
        ).order_by("name")
        self.fields["accounts"].queryset = Account.objects.filter(user=user).order_by(
            Case(When(alias="", then="name"), default="alias")
        )

    def clean(self) -> None:
        cleaned_data = super().clean()
        from_date = cleaned_data.get("from_date")
        to_date = cleaned_data.get("to_date")

        if from_date and to_date and to_date < from_date:
            self.add_error("to_date", "To date can't point before from date.")
