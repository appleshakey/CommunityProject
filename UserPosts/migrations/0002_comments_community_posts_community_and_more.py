# Generated by Django 5.0.6 on 2024-06-29 06:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Communities', '0001_initial'),
        ('UserPosts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='community',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Communities.community'),
        ),
        migrations.AddField(
            model_name='posts',
            name='community',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='Communities.community'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='UserPosts.posts'),
        ),
    ]