from django.contrib.auth.models import Group, Permission
from django.core.management.sql import emit_post_migrate_signal
from django.db import migrations, models

groups = {"Budget Supervisor Users": []}


def add_group_permissions(apps, schema_editor):
    db_alias = schema_editor.connection.alias
    emit_post_migrate_signal(2, False, "default")

    for group in groups:
        role, created = Group.objects.get_or_create(name=group)
        for permission in groups[group]:
            role.permissions.add(Permission.objects.get(codename=permission))
        role.save()


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(add_group_permissions),
    ]
