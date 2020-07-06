# Generated by Django 3.0.8 on 2020-07-06 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='admin_comment',
            field=models.CharField(blank=True, max_length=255, verbose_name='Коментарий администратора'),
        ),
        migrations.AlterField(
            model_name='test',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Активный'),
        ),
        migrations.AlterField(
            model_name='test',
            name='overview',
            field=models.TextField(max_length=2000, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='test',
            name='slug',
            field=models.SlugField(max_length=255, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='test',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название теста'),
        ),
    ]