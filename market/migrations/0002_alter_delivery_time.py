# Generated by Django 4.2.3 on 2024-01-30 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="time",
            field=models.DateField(
                choices=[(1, "1 days later"), (3, "3 days later"), (7, "7 dayss later")]
            ),
        ),
    ]
