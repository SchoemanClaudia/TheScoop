# Generated by Django 4.2.17 on 2025-01-23 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about_avatar_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaboraterequest',
            name='sent_at',
            field=models.DateField(auto_now=True),
        ),
    ]
