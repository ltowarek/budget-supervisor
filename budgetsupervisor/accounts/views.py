from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Account, Category, Connection, Transaction
from .forms import (
    CreateConnectionForm,
    ImportAccountsForm,
    ImportConnectionsForm,
    ImportTransactionsForm,
    ReportBalanceForm,
)


class IndexView(TemplateView):
    template_name = "accounts/index.html"


class ConnectionsListView(ListView):
    def get_queryset(self):
        return Connection.objects.all()


class ConnectionCreate(FormView):
    template_name = "accounts/connection_create.html"
    form_class = CreateConnectionForm
    success_url = reverse_lazy("connections:connection_import")

    def form_valid(self, form):
        redirect_url = self.request.build_absolute_uri(str(self.success_url))
        return form.create_connection(redirect_url)


class ConnectionUpdate(UpdateView):
    model = Connection
    fields = "__all__"
    success_url = reverse_lazy("connections:connection_list")


class ConnectionDelete(DeleteView):
    model = Connection
    success_url = reverse_lazy("connections:connection_list")


class ImportConnectionsView(FormView):
    template_name = "accounts/connection_import.html"
    form_class = ImportConnectionsForm
    success_url = reverse_lazy("connections:connection_list")

    def form_valid(self, form):
        form.import_connections()
        return super().form_valid(form)


class AccountListView(ListView):
    def get_queryset(self):
        return Account.objects.all()


class AccountCreate(CreateView):
    model = Account
    fields = "__all__"
    success_url = reverse_lazy("accounts:account_list")


class AccountUpdate(UpdateView):
    model = Account
    fields = "__all__"
    success_url = reverse_lazy("accounts:account_list")


class AccountDelete(DeleteView):
    model = Account
    success_url = reverse_lazy("accounts:account_list")


class ImportAccountsView(FormView):
    template_name = "accounts/account_import.html"
    form_class = ImportAccountsForm
    success_url = reverse_lazy("accounts:account_list")

    def form_valid(self, form):
        connection = form.cleaned_data["connection"]
        form.import_accounts(connection.external_id)
        return super().form_valid(form)


class TransactionListView(ListView):
    def get_queryset(self):
        accounts = self.request.GET.getlist("account_id")
        if accounts:
            return Transaction.objects.filter(account_id__in=accounts)
        return Transaction.objects.all()


class TransactionCreate(CreateView):
    model = Transaction
    fields = "__all__"
    success_url = reverse_lazy("transactions:transaction_list")


class TransactionUpdate(UpdateView):
    model = Transaction
    fields = "__all__"
    success_url = reverse_lazy("transactions:transaction_list")


class TransactionDelete(DeleteView):
    model = Transaction
    success_url = reverse_lazy("transactions:transaction_list")


class ImportTransactionsView(FormView):
    template_name = "accounts/transaction_import.html"
    form_class = ImportTransactionsForm
    success_url = reverse_lazy("transactions:transaction_list")

    def form_valid(self, form):
        account = form.cleaned_data["account"]
        form.import_transactions(account.external_id)
        return super().form_valid(form)


class CategoryListView(ListView):
    def get_queryset(self):
        return Category.objects.all()


class CategoryCreate(CreateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("categories:category_list")


class CategoryUpdate(UpdateView):
    model = Category
    fields = "__all__"
    success_url = reverse_lazy("categories:category_list")


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy("categories:category_list")


class ReportBalanceView(FormView):
    template_name = "accounts/report_balance.html"
    form_class = ReportBalanceForm
    success_url = reverse_lazy("reports:report_balance")

    def get_initial(self):
        return {
            "accounts": self.request.GET.getlist("accounts"),
            "from_date": self.request.GET.get("from_date"),
            "to_date": self.request.GET.get("to_date"),
        }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["results"] = self.form_class.get_balance(
            self.request.GET.getlist("accounts"),
            self.request.GET.get("from_date"),
            self.request.GET.get("to_date"),
        )
        return context
