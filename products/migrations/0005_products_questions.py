# Generated by Django 3.2.6 on 2021-09-29 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='questions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.questions'),
        ),
    ]