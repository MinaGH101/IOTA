# Generated by Django 5.0.6 on 2024-06-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                (
                    "name",
                    models.CharField(
                        blank=True,
                        default="Enter Your first & last name ...",
                        max_length=100,
                        null=True,
                    ),
                ),
                ("message", models.TextField()),
                (
                    "phone",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
            ],
        ),
    ]
