# Generated by Django 3.0.8 on 2020-07-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0004_auto_20200707_2359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
