# Generated by Django 4.1.6 on 2023-05-04 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0007_remove_profile_username_alter_profile_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="profile",
            name="postal_code",
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]