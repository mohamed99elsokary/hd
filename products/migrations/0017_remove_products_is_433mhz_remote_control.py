# Generated by Django 3.2.6 on 2021-10-08 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_rename_pdf1_products_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='is_433mhz_remote_control',
        ),
    ]