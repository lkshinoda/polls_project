# Generated by Django 3.0.8 on 2020-07-16 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=2000, verbose_name='Текст вопроса')),
                ('true_answer', models.CharField(max_length=50, verbose_name='Верный варинат ответа')),
                ('option_a', models.CharField(max_length=50, verbose_name='Второй вариант')),
                ('option_b', models.CharField(max_length=50, verbose_name='Третий вариант')),
                ('option_c', models.CharField(max_length=50, verbose_name='Четвертый вариант')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('admin_comment', models.CharField(blank=True, max_length=255, verbose_name='Коментарий администратора')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название теста')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('description', models.TextField(max_length=2000, verbose_name='Подробное описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('admin_comment', models.CharField(blank=True, max_length=255, verbose_name='Коментарий администратора')),
                ('question', models.ManyToManyField(related_name='tests', to='polls.Question', verbose_name='Вопросы')),
            ],
            options={
                'verbose_name': 'Тест',
                'verbose_name_plural': 'Тесты',
            },
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('description', models.TextField(max_length=2000, verbose_name='Описание')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
                ('admin_comment', models.CharField(blank=True, max_length=255, verbose_name='Коментарий администратора')),
                ('test', models.ManyToManyField(related_name='polls', to='polls.Test', verbose_name='Тесты')),
            ],
            options={
                'verbose_name': 'Опрос',
                'verbose_name_plural': 'Опросы',
            },
        ),
    ]