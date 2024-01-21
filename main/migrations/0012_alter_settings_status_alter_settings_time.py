# Generated by Django 4.2.7 on 2024-01-21 13:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_settings_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='status',
            field=models.CharField(choices=[('start', 'Запущена'), ('finish', 'Завершена'), ('created', 'Создана')], default='start', max_length=10, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 21, 18, 37, 46, 167208), verbose_name='Время рассылки'),
        ),
    ]
