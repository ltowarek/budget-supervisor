# Generated by Django 3.0.7 on 2020-07-14 21:13

from django.db import migrations, models
import django.db.models.deletion


def populate_categories(apps, schema_editor):
    Category = apps.get_model("transactions", "Category")
    names = [
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
        "Uncategorized",
    ]
    for name in names:
        category = Category(name=name)
        category.save()


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={"verbose_name_plural": "Categories",},
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField(verbose_name="transaction date")),
                ("amount", models.DecimalField(decimal_places=2, max_digits=8)),
                ("payee", models.CharField(blank=True, default="", max_length=200)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="transactions.Category",
                    ),
                ),
            ],
        ),
        migrations.RunPython(populate_categories),
    ]
