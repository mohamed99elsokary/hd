# Generated by Django 3.2.6 on 2021-10-11 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_auto_20211007_0209'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ChildModel',
        ),
        migrations.DeleteModel(
            name='ParentModel',
        ),
    ]
