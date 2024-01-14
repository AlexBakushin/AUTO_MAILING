# Generated by Django 5.0.1 on 2024-01-14 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, unique=True, verbose_name='Почта')),
                ('name', models.CharField(max_length=150, verbose_name='Имя клиента')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Logs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datatime', models.DateTimeField(auto_now=True, verbose_name='Время и дата последней попытки')),
                ('status', models.CharField(max_length=100, verbose_name='Статус попытки')),
                ('response', models.CharField(max_length=100, verbose_name='Ответ сервера')),
            ],
        ),
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=150, verbose_name='Тема письма')),
                ('body', models.TextField(verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField(default='00:00:00', verbose_name='Время рассылки')),
                ('frequency', models.CharField(choices=[('day', 'Раз в день'), ('week', 'Раз в неделю'), ('month', 'Раз в месяц')], default='day', verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('completed', 'Завершена'), ('created', 'Создана'), ('launched', 'Запущена')], default='created', max_length=10, verbose_name='Статус')),
            ],
            options={
                'verbose_name': 'Настройка',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
