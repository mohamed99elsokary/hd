# Generated by Django 3.2.6 on 2021-10-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_categories_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='video_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
