# Generated by Django 3.0.8 on 2020-07-07 18:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0002_location_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 23, 58, 56, 573479), editable=False),
        ),
    ]
