# Generated by Django 3.2.6 on 2021-09-30 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='photos'),
        ),
    ]
