# Generated by Django 3.2.6 on 2021-10-06 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0015_auto_20211006_1412'),
    ]

    operations = [
        migrations.AddField(
            model_name='files',
            name='name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to='files'),
        ),
    ]
