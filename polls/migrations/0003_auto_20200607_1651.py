# Generated by Django 3.0.7 on 2020-06-07 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20200607_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='admin_comment',
            field=models.CharField(max_length=255, verbose_name='Комментарий администратора'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_a',
            field=models.CharField(max_length=50, verbose_name='Вариант ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_b',
            field=models.CharField(max_length=50, verbose_name='Вариант ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_c',
            field=models.CharField(max_length=50, verbose_name='Вариант ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='option_d',
            field=models.CharField(max_length=50, verbose_name='Вариант ответа'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(max_length=2000, verbose_name='Текст вопросы'),
        ),
        migrations.AlterField(
            model_name='question',
            name='true_answer',
            field=models.CharField(max_length=255, verbose_name='Правильный ответ'),
        ),
    ]
