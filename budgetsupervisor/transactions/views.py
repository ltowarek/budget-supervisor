from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from .models import Category, Transaction
from .forms import ImportTransactionsForm


class TransactionListView(generic.ListView):
    def get_queryset(self):
        return Transaction.objects.all()


class TransactionCreate(CreateView):
    model = Transaction
    fields = '__all__'


class TransactionUpdate(UpdateView):
    model = Transaction
    fields = '__all__'


class TransactionDelete(DeleteView):
    model = Transaction
    success_url = reverse_lazy('transactions:transaction_list')


class CategoryListView(generic.ListView):
    def get_queryset(self):
        return Category.objects.all()


class CategoryCreate(CreateView):
    model = Category
    fields = '__all__'


class CategoryUpdate(UpdateView):
    model = Category
    fields = '__all__'


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('transactions:category')


class ImportTransactionsView(FormView):
    template_name = 'transactions/transaction_import.html'
    form_class = ImportTransactionsForm
    success_url = reverse_lazy('transactions:transaction_list')

    def form_valid(self, form):
        form.import_transactions()
        return super().form_valid(form)