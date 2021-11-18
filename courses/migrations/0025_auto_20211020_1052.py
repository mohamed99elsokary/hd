# Generated by Django 3.2.6 on 2021-10-20 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0024_auto_20211011_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='icon',
            field=models.ImageField(upload_to='courses/cover'),
        ),
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(upload_to='courses/files'),
        ),
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to='courses/course_images'),
        ),
        migrations.AlterField(
            model_name='videos',
            name='video',
            field=models.FileField(upload_to='courses/videos'),
        ),
        migrations.CreateModel(
            name='exams',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('questions', models.ManyToManyField(to='courses.Questions')),
            ],
        ),
    ]
