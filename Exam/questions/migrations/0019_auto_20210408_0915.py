# Generated by Django 3.1.3 on 2021-04-08 03:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0018_auto_20210212_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 9, 15, 38, 385392)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 8, 9, 15, 38, 385392)),
        ),
    ]