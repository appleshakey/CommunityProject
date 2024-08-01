# Generated by Django 5.0.6 on 2024-07-04 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authuser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='pincode',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='state',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.IntegerField(default=0),
        ),
    ]
