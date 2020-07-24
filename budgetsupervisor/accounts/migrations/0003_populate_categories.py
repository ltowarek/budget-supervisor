from django.db import migrations, models
import django.db.models.deletion


def populate_categories(apps, schema_editor):
    Category = apps.get_model("accounts", "Category")
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

    dependencies = [
        ("accounts", "0002_category_transaction"),
    ]

    operations = [
        migrations.RunPython(populate_categories),
    ]
