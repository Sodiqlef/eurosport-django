# Generated by Django 4.0.2 on 2022-10-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_player_all_goals_scored_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='season_joined',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
