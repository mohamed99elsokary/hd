# Generated by Django 3.2.6 on 2021-10-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_products_resistance_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]