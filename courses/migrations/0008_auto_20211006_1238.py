# Generated by Django 3.2.6 on 2021-10-06 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_alter_courses_icon'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='descreption',
            new_name='description',
        ),
        migrations.AddField(
            model_name='courses',
            name='notes',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
