from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
            verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Payee(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    class TransactionType(models.TextChoices):
        WITHDRAWAL = 'W', _('Withdrawal')
        DEPOSIT = 'D', _('Deposit')
        TRANSFER = 'T', _('Transfer')

    date = models.DateField('transaction date')
    transaction_type = models.CharField(max_length=1, choices=TransactionType.choices, default=TransactionType.WITHDRAWAL)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payee = models.ForeignKey(Payee, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)