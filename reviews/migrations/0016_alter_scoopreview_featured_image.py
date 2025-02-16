# Generated by Django 4.2.17 on 2025-01-16 22:04

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0015_alter_scoopreview_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoopreview',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/dcaygv4vw/image/upload/v1737062866/placeholder_p0airr.jpg', max_length=255, verbose_name='image'),
        ),
    ]
