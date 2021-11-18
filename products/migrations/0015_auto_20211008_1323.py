# Generated by Django 3.2.6 on 2021-10-08 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0014_auto_20211008_1237'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='pdf',
            new_name='pdf1',
        ),
        migrations.AddField(
            model_name='products',
            name='pdf2',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
        migrations.AddField(
            model_name='products',
            name='pdf3',
            field=models.FileField(blank=True, null=True, upload_to=None),
        ),
        migrations.AlterField(
            model_name='products',
            name='ampere',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='products',
            name='volt',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='products',
            name='watt',
            field=models.CharField(max_length=150),
        ),
    ]
