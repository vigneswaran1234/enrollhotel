# Generated by Django 5.0.4 on 2024-05-05 08:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="amenities",
            options={"ordering": ["uid"]},
        ),
        migrations.AlterModelOptions(
            name="hotel",
            options={"ordering": ["uid"]},
        ),
        migrations.AlterModelOptions(
            name="hotelbooking",
            options={"ordering": ["uid"]},
        ),
        migrations.AlterModelOptions(
            name="hotelimages",
            options={"ordering": ["uid"]},
        ),
    ]
