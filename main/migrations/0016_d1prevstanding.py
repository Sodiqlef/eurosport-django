# Generated by Django 4.0.2 on 2022-10-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_match_foot_note'),
    ]

    operations = [
        migrations.CreateModel(
            name='D1PrevStanding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.IntegerField(null=True)),
                ('team_details', models.TextField()),
            ],
        ),
    ]
