# Generated by Django 3.2.6 on 2021-10-06 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_categories_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='how_to_pair',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]