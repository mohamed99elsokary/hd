# Generated by Django 3.2.6 on 2021-09-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210929_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='products',
        ),
        migrations.AddField(
            model_name='questions',
            name='products',
            field=models.ManyToManyField(to='products.Products'),
        ),
    ]
