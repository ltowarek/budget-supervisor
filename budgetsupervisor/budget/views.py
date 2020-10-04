from django.views.generic import TemplateView, ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    FormMixin,
)
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import Account, Category, Connection, Transaction
from .forms import (
    CreateConnectionForm,
    ImportAccountsForm,
    ImportConnectionsForm,
    ImportTransactionsForm,
    ReportBalanceForm,
)
from saltedge_wrapper.factory import (
    connect_sessions_api,
    connections_api,
    accounts_api,
    transactions_api,
)


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "budget/index.html"


class ConnectionsListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self):
        return Connection.objects.filter(user=self.request.user).order_by("provider")


class ConnectionCreate(LoginRequiredMixin, FormView):
    template_name = "budget/connection_create.html"
    form_class = CreateConnectionForm
    success_url = reverse_lazy("connections:connection_import")

    def form_valid(self, form):
        redirect_url = self.request.build_absolute_uri(str(self.success_url))
        connect_url = Connection.objects.create_in_saltedge(
            redirect_url, self.request.user.profile.external_id, connect_sessions_api()
        )
        return redirect(connect_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["profile"] = self.request.user.profile
        return context


class ConnectionUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Connection
    fields = []
    success_url = reverse_lazy("connections:connection_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ConnectionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Connection
    success_url = reverse_lazy("connections:connection_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def delete(self, *args, **kwargs):
        connection = self.get_object()
        if connection.external_id:
            Connection.objects.remove_from_saltedge(connection, connections_api())
            # TODO: Remove external_id from related accounts/transactions.
        return super().delete(*args, **kwargs)


class ImportConnectionsView(LoginRequiredMixin, FormView):
    template_name = "budget/connection_import.html"
    form_class = ImportConnectionsForm
    success_url = reverse_lazy("connections:connection_list")

    def form_valid(self, form):
        Connection.objects.import_from_saltedge(
            self.request.user, self.request.user.profile.external_id, connections_api()
        )
        return super().form_valid(form)


class AccountListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self):
        return Account.objects.filter(user=self.request.user).order_by("name")


class AccountCreate(LoginRequiredMixin, CreateView):
    model = Account
    fields = [
        "name",
        "account_type",
    ]
    success_url = reverse_lazy("accounts:account_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class AccountUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Account
    fields = ["name", "account_type"]
    success_url = reverse_lazy("accounts:account_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class AccountDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Account
    success_url = reverse_lazy("accounts:account_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ImportAccountsView(LoginRequiredMixin, FormView):
    template_name = "budget/account_import.html"
    form_class = ImportAccountsForm
    success_url = reverse_lazy("accounts:account_list")

    def form_valid(self, form):
        connection = form.cleaned_data["connection"]
        Account.objects.import_from_saltedge(
            self.request.user, connection.external_id, accounts_api()
        )
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class TransactionListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user).order_by("-date")


class TransactionCreate(LoginRequiredMixin, CreateView):
    model = Transaction
    fields = ["date", "amount", "payee", "category", "description", "account"]
    success_url = reverse_lazy("transactions:transaction_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["account"].queryset = Account.objects.filter(user=self.request.user)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        return form


class TransactionUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Transaction
    fields = ["date", "amount", "payee", "category", "description", "account"]
    success_url = reverse_lazy("transactions:transaction_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields["account"].queryset = Account.objects.filter(user=self.request.user)
        form.fields["category"].queryset = Category.objects.filter(
            user=self.request.user
        )
        return form


class TransactionDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Transaction
    success_url = reverse_lazy("transactions:transaction_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ImportTransactionsView(LoginRequiredMixin, FormView):
    template_name = "budget/transaction_import.html"
    form_class = ImportTransactionsForm
    success_url = reverse_lazy("transactions:transaction_list")

    def form_valid(self, form):
        account = form.cleaned_data["account"]
        Transaction.objects.import_from_saltedge(
            self.request.user,
            account.connection.external_id,
            account.external_id,
            transactions_api(),
        )
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs


class CategoryListView(LoginRequiredMixin, ListView):
    paginate_by = 25

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user).order_by("name")


class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    fields = ["name"]
    success_url = reverse_lazy("categories:category_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class CategoryUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    fields = ["name"]
    success_url = reverse_lazy("categories:category_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class CategoryDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("categories:category_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ReportBalanceView(LoginRequiredMixin, FormMixin, TemplateView):
    template_name = "budget/report_balance.html"
    form_class = ReportBalanceForm

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.GET:
            kwargs["data"] = self.request.GET
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        balance = Transaction.objects.get_balance(
            form.cleaned_data["accounts"],
            self.request.user,
            form.cleaned_data["from_date"],
            form.cleaned_data["to_date"],
        )
        return self.render_to_response(
            self.get_context_data(form=form, balance=balance)
        )
