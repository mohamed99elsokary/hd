# Generated by Django 3.2.6 on 2021-10-06 21:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_lectures_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.FileField(upload_to='files')),
                ('description_before', models.TextField()),
                ('description_after', models.TextField()),
                ('notes', models.TextField()),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.lectures')),
            ],
        ),
    ]