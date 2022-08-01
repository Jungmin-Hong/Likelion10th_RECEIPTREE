# Generated by Django 4.0.6 on 2022-08-01 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='team_no',
            field=models.ForeignKey(db_column='team_no', null=True, on_delete=django.db.models.deletion.CASCADE, to='home.team'),
        ),
    ]