# Generated by Django 4.0.6 on 2022-08-13 00:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0004_alter_team_board_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ['-team_date']},
        ),
        migrations.AddField(
            model_name='team',
            name='team_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]