# Generated by Django 3.2.6 on 2021-10-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_auto_20211013_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='tools',
            name='icon',
            field=models.ImageField(default='', upload_to='tools'),
            preserve_default=False,
        ),
    ]
