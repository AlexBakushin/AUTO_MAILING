# Generated by Django 4.2.7 on 2024-01-21 15:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_settings_status_alter_settings_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 21, 20, 48, 43, 632258), verbose_name='Время рассылки'),
        ),
    ]
