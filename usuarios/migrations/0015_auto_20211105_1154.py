# Generated by Django 3.2.7 on 2021-11-05 17:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0014_auto_20211105_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 11, 54, 2, 734401)),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 5, 11, 54, 2, 734401)),
        ),
    ]
