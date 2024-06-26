# Generated by Django 5.0.1 on 2024-01-30 15:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0003_alter_delivery_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="time",
            field=models.DateField(
                choices=[
                    (datetime.datetime(2024, 1, 31, 15, 17, 52, 5366), "1 day later"),
                    (datetime.datetime(2024, 2, 2, 15, 17, 52, 5366), "3 days later"),
                    (datetime.datetime(2024, 2, 6, 15, 17, 52, 5366), "7 days later"),
                ]
            ),
        ),
    ]
