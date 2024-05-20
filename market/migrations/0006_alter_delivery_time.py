# Generated by Django 5.0.1 on 2024-01-30 15:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("market", "0005_alter_delivery_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="delivery",
            name="time",
            field=models.CharField(
                choices=[
                    ("one", "one day later"),
                    ("three", "three days later"),
                    ("seven", "seven days later"),
                ],
                max_length=50,
            ),
        ),
    ]
