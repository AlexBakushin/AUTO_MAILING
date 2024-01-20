# Generated by Django 5.0.1 on 2024-01-20 15:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_client_user_alter_settings_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='user',
        ),
        migrations.AlterField(
            model_name='settings',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 20, 20, 37, 24, 109654), verbose_name='Время рассылки'),
        ),
    ]
