# Generated by Django 3.1.3 on 2020-12-26 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankdb_app', '0005_auto_20201226_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounttable',
            name='account_password',
            field=models.CharField(default=None, max_length=32),
        ),
        migrations.AlterField(
            model_name='transactiontable',
            name='date_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 26, 16, 47, 41, 725534)),
        ),
    ]