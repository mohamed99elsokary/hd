# Generated by Django 3.2.6 on 2021-10-06 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_auto_20211006_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectures',
            name='description',
        ),
        migrations.RemoveField(
            model_name='lectures',
            name='notes',
        ),
        migrations.AddField(
            model_name='videos',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
