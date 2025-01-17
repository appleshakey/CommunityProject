# Generated by Django 5.0.6 on 2024-06-27 08:22

import django.utils.timezone
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('created_now', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
