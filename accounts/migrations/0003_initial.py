# Generated by Django 4.1.6 on 2023-05-04 05:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("accounts", "0002_delete_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                (
                    "first_name",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
                ("phone", models.IntegerField(blank=True, default=None, null=True)),
                (
                    "address1",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
                (
                    "address2",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
                (
                    "state",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
                (
                    "area",
                    models.CharField(
                        blank=True, default=None, max_length=50, null=True
                    ),
                ),
                (
                    "postal_code",
                    models.IntegerField(blank=True, default=None, null=True),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
