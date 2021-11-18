# Generated by Django 3.2.6 on 2021-10-06 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_videos_video'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videos',
            old_name='video_link',
            new_name='description',
        ),
        migrations.AddField(
            model_name='files',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]