# Generated by Django 3.1.3 on 2021-09-10 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankdb_app', '0007_auto_20210910_1024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transactiontable',
            name='date_time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 10, 11, 4, 35, 132865)),
        ),
    ]