# Generated by Django 4.2.17 on 2025-01-09 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_rename_heading_scoopreview_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoopreview',
            name='blurb',
            field=models.TextField(blank=True),
        ),
    ]
