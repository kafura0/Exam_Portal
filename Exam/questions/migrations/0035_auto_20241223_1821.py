# Generated by Django 3.2.25 on 2024-12-23 15:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0034_auto_20241223_1819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 23, 18, 21, 27, 608366)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 23, 18, 21, 27, 608366)),
        ),
    ]
