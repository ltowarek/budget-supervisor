from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Account, Category, Transaction
from .forms import ImportAccountsForm, ImportTransactionsForm


class AccountListView(generic.ListView):
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
        form.import_accounts()
        return super().form_valid(form)


class TransactionListView(generic.ListView):
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
        account = Account.objects.get(pk=self.kwargs["account_id"])
        form.import_transactions(account.external_id)
        return super().form_valid(form)


class CategoryListView(generic.ListView):
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
