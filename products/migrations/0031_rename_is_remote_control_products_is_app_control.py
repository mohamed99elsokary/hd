# Generated by Django 3.2.6 on 2021-10-13 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0030_tools_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='is_remote_control',
            new_name='is_app_control',
        ),
    ]
