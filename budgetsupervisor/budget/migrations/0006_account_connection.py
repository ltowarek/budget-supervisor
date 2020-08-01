# Generated by Django 3.0.7 on 2020-08-01 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("budget", "0005_connection"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="connection",
            field=models.ForeignKey(
                blank=True,
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="budget.Connection",
            ),
        ),
    ]
