# Generated by Django 4.0.2 on 2022-10-16 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_match_match_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='match_status',
        ),
        migrations.AddField(
            model_name='match',
            name='competition',
            field=models.CharField(choices=[('Division 1 League', 'Division 1 League'), ('Division 2 League ', 'Division 2 League'), ('League Cup, Division 1', 'League Cup, Division 1'), ('League Cup, Division 2', 'League Cup, Division 2'), ('Champions League', 'Champions League'), ('Europa League', 'Europa League'), ('Super Cup', 'Super Cup'), ('International Match', 'International Match')], max_length=100, null=True),
        ),
    ]
