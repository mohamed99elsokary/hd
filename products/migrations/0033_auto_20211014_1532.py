# Generated by Django 3.2.6 on 2021-10-14 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_auto_20211014_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questions',
            name='ar_answer',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='ar_question',
        ),
        migrations.AddField(
            model_name='questions',
            name='answer',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='questions',
            name='question',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='ar_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='ar_how_to_pair',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tools',
            name='ar_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]