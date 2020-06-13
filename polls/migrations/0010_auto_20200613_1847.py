# Generated by Django 3.0.7 on 2020-06-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0009_auto_20200613_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='test',
            field=models.ManyToManyField(related_name='polls', to='polls.Test'),
        ),
        migrations.AlterField(
            model_name='test',
            name='question',
            field=models.ManyToManyField(related_name='tests', to='polls.Question'),
        ),
    ]
