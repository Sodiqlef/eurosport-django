# Generated by Django 4.0.2 on 2022-10-16 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_standing_alter_match_away_goal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='D1Standing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.IntegerField()),
                ('club', models.CharField(max_length=50)),
                ('mp', models.IntegerField()),
                ('w', models.IntegerField()),
                ('d', models.IntegerField()),
                ('l', models.IntegerField()),
                ('pts', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='D2Standing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pos', models.IntegerField()),
                ('club', models.CharField(max_length=50)),
                ('mp', models.IntegerField()),
                ('w', models.IntegerField()),
                ('d', models.IntegerField()),
                ('l', models.IntegerField()),
                ('pts', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Standing',
        ),
    ]
