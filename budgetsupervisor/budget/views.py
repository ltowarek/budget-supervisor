from django.views.generic import TemplateView, ListView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
    FormMixin,
)
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
    template_name = "budget/index.html"


class ConnectionsListView(ListView):
    paginate_by = 25

    def get_queryset(self):
        return Connection.objects.all()


class ConnectionCreate(FormView):
    template_name = "budget/connection_create.html"
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
    template_name = "budget/connection_import.html"
    form_class = ImportConnectionsForm
    success_url = reverse_lazy("connections:connection_list")

    def form_valid(self, form):
        form.import_connections()
        return super().form_valid(form)


class AccountListView(ListView):
    paginate_by = 25

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
    template_name = "budget/account_import.html"
    form_class = ImportAccountsForm
    success_url = reverse_lazy("accounts:account_list")

    def form_valid(self, form):
        connection = form.cleaned_data["connection"]
        form.import_accounts(connection.external_id)
        return super().form_valid(form)


class TransactionListView(ListView):
    paginate_by = 25

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
    template_name = "budget/transaction_import.html"
    form_class = ImportTransactionsForm
    success_url = reverse_lazy("transactions:transaction_list")

    def form_valid(self, form):
        account = form.cleaned_data["account"]
        form.import_transactions(account.external_id, account.connection.external_id)
        return super().form_valid(form)


class CategoryListView(ListView):
    paginate_by = 25

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


class ReportBalanceView(FormMixin, TemplateView):
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
        return kwargs

    def form_valid(self, form):
        balance = form.get_balance(
            form.cleaned_data["accounts"],
            form.cleaned_data["from_date"],
            form.cleaned_data["to_date"],
        )
        return self.render_to_response(
            self.get_context_data(form=form, balance=balance)
        )
