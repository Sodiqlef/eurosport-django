# Generated by Django 4.0.2 on 2022-10-21 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0023_rename_currentseason_currentedition_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Currentedition',
            new_name='Currentseason',
        ),
        migrations.AlterModelOptions(
            name='currentseason',
            options={'verbose_name_plural': 'Current season'},
        ),
        migrations.RenameField(
            model_name='currentseason',
            old_name='current_edition',
            new_name='current_season',
        ),
        migrations.RenameField(
            model_name='d1standing',
            old_name='edition',
            new_name='season',
        ),
        migrations.RenameField(
            model_name='d2standing',
            old_name='edition',
            new_name='season',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='edition',
            new_name='season',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='edition_joined',
            new_name='season_joined',
        ),
    ]
