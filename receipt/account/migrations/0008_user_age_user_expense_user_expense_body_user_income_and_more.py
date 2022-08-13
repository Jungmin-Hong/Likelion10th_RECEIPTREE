# Generated by Django 4.0.6 on 2022-08-13 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='expense',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='expense_body',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='income',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='job',
            field=models.CharField(max_length=40, null=True),
        ),
    ]