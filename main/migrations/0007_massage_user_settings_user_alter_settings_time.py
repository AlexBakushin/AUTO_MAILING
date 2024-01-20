# Generated by Django 4.2.7 on 2024-01-20 17:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0006_client_user_alter_settings_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='massage',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AddField(
            model_name='settings',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 20, 22, 10, 11, 680698), verbose_name='Время рассылки'),
        ),
    ]