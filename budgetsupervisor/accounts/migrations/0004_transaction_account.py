# Generated by Django 3.0.7 on 2020-07-24 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_populate_categories"),
    ]

    operations = [
        migrations.AddField(
            model_name="transaction",
            name="account",
            field=models.ForeignKey(
                default=2,
                on_delete=django.db.models.deletion.CASCADE,
                to="accounts.Account",
            ),
            preserve_default=False,
        ),
    ]