# Generated by Django 3.0.7 on 2020-07-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_answer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='is_true',
            field=models.BooleanField(default=False, verbose_name='Правильный ответ'),
        ),
    ]