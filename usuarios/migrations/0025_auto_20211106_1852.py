# Generated by Django 3.2.7 on 2021-11-07 00:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0024_auto_20211106_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 18, 52, 44, 311098)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 6, 18, 52, 44, 311098)),
        ),
    ]
