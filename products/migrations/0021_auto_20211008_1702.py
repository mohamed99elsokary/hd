# Generated by Django 3.2.6 on 2021-10-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_products_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='programing_video_1',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='products',
            name='programing_video_2',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
