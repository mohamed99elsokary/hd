# Generated by Django 3.2.6 on 2021-10-08 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0022_auto_20211008_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='digram_2',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
