# Generated by Django 4.2.17 on 2025-01-14 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_alter_scoopreview_blurb'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoopreview',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
