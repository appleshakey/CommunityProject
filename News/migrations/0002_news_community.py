# Generated by Django 5.0.6 on 2024-06-29 06:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Communities', '0001_initial'),
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='community',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Communities.community'),
        ),
    ]