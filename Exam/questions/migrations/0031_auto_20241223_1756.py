# Generated by Django 3.2.25 on 2024-12-23 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0030_auto_20240926_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam_model',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 23, 17, 56, 39, 47228)),
        ),
        migrations.AlterField(
            model_name='exam_model',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 23, 17, 56, 39, 47228)),
        ),
    ]
