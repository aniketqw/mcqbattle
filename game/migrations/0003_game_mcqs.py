# Generated by Django 5.0.6 on 2024-08-01 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_game_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='mcqs',
            field=models.JSONField(default=dict),
        ),
    ]
