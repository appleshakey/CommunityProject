# Generated by Django 5.0.6 on 2024-08-01 12:45

import Communities.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Communities', '0003_alter_community_secret_key'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='photo',
            field=models.FileField(blank=True, upload_to=Communities.models.upload_to),
        ),
    ]