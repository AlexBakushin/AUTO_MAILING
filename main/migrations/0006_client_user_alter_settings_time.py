# Generated by Django 5.0.1 on 2024-01-20 15:56

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_client_user_alter_settings_time'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 20, 20, 56, 20, 448006), verbose_name='Время рассылки'),
        ),
    ]
