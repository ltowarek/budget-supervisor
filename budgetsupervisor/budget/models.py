import swagger_client as saltedge_client
from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _


class ConnectionManager(models.Manager):
    def create_in_saltedge(self, redirect_url, customer_id, connect_sessions_api):
        attempt = saltedge_client.AttemptRequestBody(
            return_to=redirect_url, store_credentials=False
        )
        consent = saltedge_client.ConsentRequestBody(
            scopes=["account_details", "transactions_details"]
        )
        data = saltedge_client.ConnectSessionRequestBodyData(
            str(customer_id), consent, attempt=attempt
        )
        body = saltedge_client.ConnectSessionRequestBody(data)
        response = connect_sessions_api.connect_sessions_create_post(body=body)
        return response.data.connect_url

    def import_from_saltedge(self, user, customer_id, connections_api):
        response = connections_api.connections_get(str(customer_id))
        new_connections = []
        for imported_connection in response.data:
            imported_id = int(imported_connection.id)

            c, created = Connection.objects.update_or_create(
                external_id=imported_id,
                defaults={"provider": imported_connection.provider_name, "user": user},
            )
            if created:
                new_connections.append(c)
        return new_connections

    def remove_from_saltedge(self, connection, connections_api):
        connections_api.connections_connection_id_delete(str(connection.external_id))
        connection.external_id = None
        connection.save()


class Connection(models.Model):
    provider = models.CharField(max_length=200, editable=False)
    # TODO: Can external_id be set to null?
    # Connection without external_id makes no sense.
    external_id = models.BigIntegerField(blank=True, null=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = ConnectionManager()

    def __str__(self):
        return str(self.provider)


class AccountManager(models.Manager):
    def import_from_saltedge(self, user, connection_id, accounts_api):
        response = accounts_api.accounts_get(str(connection_id))
        new_accounts = []
        for imported_account in response.data:
            imported_id = int(imported_account.id)

            a, created = Account.objects.update_or_create(
                external_id=imported_id,
                defaults={
                    "name": imported_account.name,
                    "account_type": Account.AccountType.ACCOUNT,
                    "connection": Connection.objects.get(external_id=connection_id),
                    "user": user,
                },
            )
            if created:
                new_accounts.append(a)
        return new_accounts


class Account(models.Model):
    class AccountType(models.TextChoices):
        ACCOUNT = "A", _("Bank account")
        CASH = "C", _("Cash")

    name = models.CharField(max_length=200)
    account_type = models.CharField(
        max_length=1, choices=AccountType.choices, default=AccountType.ACCOUNT
    )
    external_id = models.BigIntegerField(blank=True, null=True, editable=False)
    # TODO: If connection is removed then related accounts should not be deleted
    connection = models.ForeignKey(
        Connection, on_delete=models.CASCADE, blank=True, null=True, editable=False
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = AccountManager()

    def __str__(self):
        return str(self.name)


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return str(self.name)


def populate_user_categories(sender, instance, created, **kwargs):
    if created:
        categories = [
            "Auto and Transport",
            "Bills and Utilities",
            "Education",
            "Entertainment",
            "Fees and Charges",
            "Food and Dining",
            "Gifts and Donations",
            "Health and Fitness",
            "Home",
            "Income",
            "Insurance",
            "Kids",
            "Pets",
            "Shopping",
            "Transfer",
            "Travel",
            # TODO: Replace Uncategorized with simple None/null category.
            "Uncategorized",
        ]
        for category in categories:
            Category.objects.create(name=category, user=instance)


post_save.connect(populate_user_categories, sender=settings.AUTH_USER_MODEL)


class TransactionManager(models.Manager):
    def import_from_saltedge(self, user, connection_id, account_id, transactions_api):
        response = transactions_api.transactions_get(
            str(connection_id), account_id=str(account_id)
        )
        uncategorized = Category.objects.get(name="Uncategorized", user=user)
        new_transactions = []
        for imported_transaction in response.data:
            imported_id = int(imported_transaction.id)

            escaped_category = imported_transaction.category.replace("_", " ")
            category = Category.objects.filter(name__iexact=escaped_category, user=user)
            category = category[0] if category else uncategorized

            t, created = Transaction.objects.update_or_create(
                external_id=imported_id,
                defaults={
                    "date": imported_transaction.made_on,
                    "amount": imported_transaction.amount,
                    "payee": "",
                    "category": category,
                    "description": imported_transaction.description,
                    "account_id": Account.objects.get(
                        external_id=imported_transaction.account_id
                    ).id,
                    "user": user,
                },
            )
            if created:
                new_transactions.append(t)
        return new_transactions

    def get_balance(self, accounts, user, from_date=None, to_date=None):
        q = {"account__in": accounts, "user": user}
        if from_date:
            q["date__gte"] = from_date
        if to_date:
            q["date__lte"] = to_date

        queryset = (
            Transaction.objects.filter(**q)
            .values("category__name")
            .annotate(Sum("amount"))
        )
        balance = {d["category__name"]: d["amount__sum"] for d in queryset}
        balance["Total"] = sum(balance.values())
        return balance


class Transaction(models.Model):
    date = models.DateField("transaction date")
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payee = models.CharField(max_length=200, blank=True, default="")
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True
    )
    description = models.CharField(max_length=200, blank=True, default="")
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    external_id = models.BigIntegerField(blank=True, null=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    objects = TransactionManager()

    def __str__(self):
        return str(self.description)
