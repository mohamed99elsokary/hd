# Generated by Django 3.2.6 on 2021-09-29 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_questions'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='questions',
        ),
        migrations.AddField(
            model_name='questions',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.products'),
        ),
    ]
