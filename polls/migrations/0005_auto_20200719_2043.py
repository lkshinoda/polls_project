# Generated by Django 3.0.7 on 2020-07-19 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20200719_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer', to='polls.Question', verbose_name='Вопрос'),
        ),
    ]
