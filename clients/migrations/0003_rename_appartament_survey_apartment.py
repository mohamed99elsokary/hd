# Generated by Django 3.2.6 on 2021-10-13 12:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_remove_client_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='survey',
            old_name='appartament',
            new_name='apartment',
        ),
    ]