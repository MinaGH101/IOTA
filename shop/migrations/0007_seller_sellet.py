# Generated by Django 4.1.6 on 2023-05-05 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_remove_shipping_address_remove_shipping_city_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="seller",
            name="sellet",
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]