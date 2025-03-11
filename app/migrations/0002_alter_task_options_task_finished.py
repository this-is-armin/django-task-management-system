# Generated by Django 4.2.7 on 2025-03-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created', '-finished']},
        ),
        migrations.AddField(
            model_name='task',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
