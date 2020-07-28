from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class Connection(models.Model):
    provider = models.CharField(max_length=200, editable=False)
    external_id = models.BigIntegerField(blank=True, null=True, editable=False)

    def __str__(self):
        return str(self.provider)


class Account(models.Model):
    class AccountType(models.TextChoices):
        ACCOUNT = "A", _("Bank account")
        CASH = "C", _("Cash")

    name = models.CharField(max_length=200)
    account_type = models.CharField(
        max_length=1, choices=AccountType.choices, default=AccountType.ACCOUNT
    )
    external_id = models.BigIntegerField(blank=True, null=True, editable=False)

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


class Transaction(models.Model):
    date = models.DateField("transaction date")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payee = models.CharField(max_length=200, blank=True, default="")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, blank=True, default="")
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    external_id = models.BigIntegerField(blank=True, null=True, editable=False)

    def __str__(self):
        return str(self.id)
