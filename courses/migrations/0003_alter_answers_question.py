# Generated by Django 3.2.6 on 2021-10-03 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20211003_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.questions'),
        ),
    ]
