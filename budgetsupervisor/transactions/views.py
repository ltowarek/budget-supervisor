from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Category, Transaction


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
    success_url = reverse_lazy('transactions')


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
    success_url = reverse_lazy('transactions/category')

