# Generated by Django 4.0.2 on 2022-10-17 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_currentseason'),
    ]

    operations = [
        migrations.AddField(
            model_name='d2standing',
            name='season',
            field=models.IntegerField(null=True),
        ),
    ]
