# Generated by Django 3.2.6 on 2021-10-11 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_alter_products_video_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='quick_start',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
    ]
