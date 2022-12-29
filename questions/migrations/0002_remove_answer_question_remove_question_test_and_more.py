# Generated by Django 4.1.4 on 2022-12-29 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='question',
            name='test',
        ),
        migrations.AddField(
            model_name='question',
            name='answers',
            field=models.ManyToManyField(blank=True, to='questions.answer'),
        ),
    ]
