from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
            verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    date = models.DateField('transaction date')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payee = models.CharField(max_length=200, blank=True, default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)