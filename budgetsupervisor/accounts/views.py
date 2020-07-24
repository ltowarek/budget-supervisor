from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Account
from .forms import ImportAccountsForm


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
