from typing import Any, Dict, List

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.forms import ModelForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    FormMixin,
    FormView,
    UpdateView,
)
from saltedge_wrapper.factory import (
    accounts_api,
    connect_sessions_api,
    connections_api,
    transactions_api,
)

from .forms import (
    CreateConnectionForm,
    ImportAccountsForm,
    ImportConnectionsForm,
    ImportTransactionsForm,
    ReportBalanceForm,
)
from .models import Account, Category, Connection, Transaction


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "budget/index.html"


class ConnectionsListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self) -> QuerySet:
        return Connection.objects.filter(user=self.request.user).order_by("provider")


class ConnectionCreate(LoginRequiredMixin, FormView):
    template_name = "budget/connection_create.html"
    form_class = CreateConnectionForm
    success_url = reverse_lazy("connections:connection_import")

    def form_valid(self, form: CreateConnectionForm) -> HttpResponseRedirect:
        redirect_url = self.request.build_absolute_uri(str(self.success_url))
        connect_url = Connection.objects.create_in_saltedge(
            redirect_url, self.request.user.profile.external_id, connect_sessions_api()
        )
        return redirect(connect_url)

    def get_context_data(self, **kwargs: Any) -> Dict:
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.profile
        return context


class ConnectionUpdate(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Connection
    fields: List[str] = []
    success_url = reverse_lazy("connections:connection_list")
    success_message = "Connection was updated successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user


class ConnectionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Connection
    success_url = reverse_lazy("connections:connection_list")
    success_message = "Connection was deleted successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        connection = self.get_object()
        if connection.external_id:
            Connection.objects.remove_from_saltedge(connection, connections_api())
            # TODO: Remove external_id from related accounts/transactions.
        output = super().delete(*args, **kwargs)
        messages.success(self.request, self.success_message)
        return output


class ImportConnectionsView(LoginRequiredMixin, FormView):
    template_name = "budget/connection_import.html"
    form_class = ImportConnectionsForm
    success_url = reverse_lazy("connections:connection_list")
    success_message = "Connections were imported successfully: {}"

    def form_valid(self, form: ImportConnectionsForm) -> HttpResponseRedirect:
        imported = Connection.objects.import_from_saltedge(
            self.request.user, self.request.user.profile.external_id, connections_api()
        )
        messages.success(self.request, self.success_message.format(len(imported)))
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> Dict:
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.profile
        return context


class AccountListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self) -> QuerySet:
        return Account.objects.filter(user=self.request.user).order_by("name")


class AccountCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Account
    fields = [
        "name",
        "account_type",
    ]
    success_url = reverse_lazy("accounts:account_list")
    success_message = "Account was created successfully"

    def form_valid(self, form: ModelForm) -> HttpResponseRedirect:
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdate(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Account
    fields = ["name", "account_type"]
    success_url = reverse_lazy("accounts:account_list")
    success_message = "Account was updated successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user


class AccountDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Account
    success_url = reverse_lazy("accounts:account_list")
    success_message = "Account was deleted successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        output = super().delete(*args, **kwargs)
        messages.success(self.request, self.success_message)
        return output


class ImportAccountsView(LoginRequiredMixin, FormView):
    template_name = "budget/account_import.html"
    form_class = ImportAccountsForm
    success_url = reverse_lazy("accounts:account_list")
    success_message = "Accounts were imported successfully: {}"

    def form_valid(self, form: ImportAccountsForm) -> HttpResponseRedirect:
        connection = form.cleaned_data["connection"]
        imported = Account.objects.import_from_saltedge(
            self.request.user, connection.external_id, accounts_api()
        )
        messages.success(self.request, self.success_message.format(len(imported)))
        return super().form_valid(form)

    def get_form_kwargs(self) -> Dict:
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs: Any) -> Dict:
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.profile
        return context


class TransactionListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self) -> QuerySet:
        return Transaction.objects.filter(user=self.request.user).order_by("-date")


class TransactionCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Transaction
    fields = ["date", "amount", "payee", "category", "description", "account"]
    success_url = reverse_lazy("transactions:transaction_list")
    success_message = "Transaction was created successfully"

    def form_valid(self, form: ModelForm) -> HttpResponseRedirect:
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, *args: Any, **kwargs: Any) -> ModelForm:
        form = super().get_form(*args, **kwargs)
        form.fields["account"].queryset = Account.objects.filter(user=self.request.user)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        return form


class TransactionUpdate(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Transaction
    fields = ["date", "amount", "payee", "category", "description", "account"]
    success_url = reverse_lazy("transactions:transaction_list")
    success_message = "Transaction was updated successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def get_form(self, *args: Any, **kwargs: Any) -> ModelForm:
        form = super().get_form(*args, **kwargs)
        form.fields["account"].queryset = Account.objects.filter(user=self.request.user)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        return form


class TransactionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy("transactions:transaction_list")
    success_message = "Transaction was deleted successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        output = super().delete(*args, **kwargs)
        messages.success(self.request, self.success_message)
        return output


class ImportTransactionsView(LoginRequiredMixin, FormView):
    template_name = "budget/transaction_import.html"
    form_class = ImportTransactionsForm
    success_url = reverse_lazy("transactions:transaction_list")
    success_message = "Transactions were imported successfully: {}"

    def form_valid(self, form: ImportTransactionsForm) -> HttpResponseRedirect:
        account = form.cleaned_data["account"]
        imported = Transaction.objects.import_from_saltedge(
            self.request.user,
            account.connection.external_id,
            account.external_id,
            transactions_api(),
        )
        messages.success(self.request, self.success_message.format(len(imported)))
        return super().form_valid(form)

    def get_form_kwargs(self) -> Dict:
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs: Any) -> Dict:
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.profile
        return context


class CategoryListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self) -> QuerySet:
        return Category.objects.filter(user=self.request.user).order_by("name")


class CategoryCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ["name"]
    success_url = reverse_lazy("categories:category_list")
    success_message = "Category was created successfully"

    def form_valid(self, form: ModelForm) -> HttpResponseRedirect:
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdate(
    LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView
):
    model = Category
    fields = ["name"]
    success_url = reverse_lazy("categories:category_list")
    success_message = "Category was updated successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user


class CategoryDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("categories:category_list")
    success_message = "Category was deleted successfully"

    def test_func(self) -> bool:
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, *args: Any, **kwargs: Any) -> HttpResponseRedirect:
        output = super().delete(*args, **kwargs)
        messages.success(self.request, self.success_message)
        return output


class ReportBalanceView(LoginRequiredMixin, FormMixin, TemplateView):
    template_name = "budget/report_balance.html"
    form_class = ReportBalanceForm

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form_kwargs(self) -> Dict:
        kwargs = super().get_form_kwargs()
        if self.request.GET:
            kwargs["data"] = self.request.GET
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form: ReportBalanceForm) -> HttpResponse:
        balance = Transaction.objects.get_balance(
            form.cleaned_data["accounts"],
            self.request.user,
            form.cleaned_data["from_date"],
            form.cleaned_data["to_date"],
        )
        return self.render_to_response(
            self.get_context_data(form=form, balance=balance)
        )
