# Generated by Django 3.2.6 on 2021-10-20 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0027_auto_20211020_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='lecture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.lectures'),
        ),
    ]
