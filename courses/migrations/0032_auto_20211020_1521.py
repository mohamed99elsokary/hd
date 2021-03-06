# Generated by Django 3.2.6 on 2021-10-20 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0031_delete_final_exams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answers',
            name='question',
        ),
        migrations.RemoveField(
            model_name='questions',
            name='lecture',
        ),
        migrations.AddField(
            model_name='lectures',
            name='questions',
            field=models.ManyToManyField(to='courses.Questions'),
        ),
        migrations.AddField(
            model_name='questions',
            name='answers',
            field=models.ManyToManyField(related_name='question_answers', to='courses.Answers'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='right_answer',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='right_answer', to='courses.answers'),
        ),
    ]
