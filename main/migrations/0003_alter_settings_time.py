# Generated by Django 5.0.1 on 2024-01-20 15:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_settings_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 20, 20, 4, 56, 708124), verbose_name='Время рассылки'),
        ),
    ]
