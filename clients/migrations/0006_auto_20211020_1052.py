# Generated by Django 3.2.6 on 2021-10-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_offer_is_accepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='offer',
            name='offer',
            field=models.FileField(upload_to='client/offer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order',
            field=models.FileField(upload_to='client/order'),
        ),
        migrations.AlterField(
            model_name='products_in_rooms',
            name='after',
            field=models.ImageField(blank=True, null=True, upload_to='client/after'),
        ),
        migrations.AlterField(
            model_name='products_in_rooms',
            name='before',
            field=models.ImageField(blank=True, null=True, upload_to='client/before'),
        ),
        migrations.AlterField(
            model_name='survey',
            name='survey',
            field=models.FileField(upload_to='client/survey/'),
        ),
    ]
