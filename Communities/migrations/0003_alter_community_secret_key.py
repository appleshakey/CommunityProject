# Generated by Django 5.0.6 on 2024-06-29 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Communities', '0002_community_secret_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='secret_key',
            field=models.CharField(default='', max_length=100, unique=True),
        ),
    ]
