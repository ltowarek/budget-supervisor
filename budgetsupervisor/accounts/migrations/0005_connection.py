# Generated by Django 3.0.7 on 2020-07-25 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0004_transaction_account"),
    ]

    operations = [
        migrations.CreateModel(
            name="Connection",
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
                ("provider", models.CharField(editable=False, max_length=200)),
                (
                    "external_id",
                    models.BigIntegerField(blank=True, editable=False, null=True),
                ),
            ],
        ),
    ]
