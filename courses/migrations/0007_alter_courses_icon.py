# Generated by Django 3.2.6 on 2021-10-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_alter_courses_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='icon',
            field=models.ImageField(default='', upload_to='photos/courses'),
            preserve_default=False,
        ),
    ]
