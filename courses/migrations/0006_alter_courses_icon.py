# Generated by Django 3.2.6 on 2021-10-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20211005_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='icon',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/courses'),
        ),
    ]