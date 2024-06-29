# Generated by Django 5.0.6 on 2024-06-29 06:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Communities', '0001_initial'),
        ('Events', '0002_events_event_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='community',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Communities.community'),
        ),
    ]