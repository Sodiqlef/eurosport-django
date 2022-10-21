# Generated by Django 4.0.2 on 2022-10-21 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_remove_d1standing_pos'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Currentseason',
            new_name='Currentedition',
        ),
        migrations.AlterModelOptions(
            name='currentedition',
            options={'verbose_name_plural': 'Current edition'},
        ),
        migrations.RenameField(
            model_name='currentedition',
            old_name='current_season',
            new_name='current_edition',
        ),
        migrations.RenameField(
            model_name='d1standing',
            old_name='season',
            new_name='edition',
        ),
        migrations.RenameField(
            model_name='d2standing',
            old_name='season',
            new_name='edition',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='season',
            new_name='edition',
        ),
        migrations.RenameField(
            model_name='player',
            old_name='season_joined',
            new_name='edition_joined',
        ),
    ]
