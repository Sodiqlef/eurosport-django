# Generated by Django 4.0.2 on 2022-10-17 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_d1standing_season'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currentseason',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_season', models.IntegerField()),
            ],
        ),
    ]
