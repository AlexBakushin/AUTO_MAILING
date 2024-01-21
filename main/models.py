from django.db import models
from datetime import datetime
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}  # шаблон для необязательного элемента


class Logs(models.Model):
    STATUS_TYPES = [
        ('start', 'Запущена'),
        ('finish', 'Завершена'),
        ('created', 'Создана')
    ]

    datatime = models.DateTimeField(verbose_name='Время и дата последней попытки', auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_TYPES, default='created', verbose_name='Статус')
    response = models.CharField(max_length=100, verbose_name='Ответ сервера', )

    def __str__(self):
        return f'{self.status}, {self.response}, {self.datatime}'

    class Meta:
        verbose_name = 'Логи'
        verbose_name_plural = 'Логи'


class Massage(models.Model):
    head = models.CharField(max_length=150, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')
    logs = models.ManyToManyField(Logs, verbose_name='Логи', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                             verbose_name='Пользователь')

    def __str__(self):
        return f'{self.head}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'


class Client(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', **NULLABLE)
    sur_name = models.CharField(max_length=150, verbose_name='Отчество', **NULLABLE)
    mail = models.EmailField(unique=True, verbose_name='Почта')
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                             verbose_name='Пользователь')

    def __str__(self):
        return f'{self.mail}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Settings(models.Model):
    STATUS_TYPES = [
        ('start', 'Запущена'),
        ('finish', 'Завершена'),
        ('created', 'Создана')
    ]

    FREQUENCY_TYPES = [
        ('once_a_day', 'Раз в день'),
        ('once_a_week', 'Раз в неделю'),
        ('once_a_month', 'Раз в месяц')
    ]

    time = models.DateTimeField(verbose_name='Время рассылки', default=datetime.now())
    frequency = models.CharField(default='Раз в день', choices=FREQUENCY_TYPES, verbose_name='Периодичность')
    status = models.CharField(max_length=10, default='start', choices=STATUS_TYPES, verbose_name='Статус')
    client = models.ManyToManyField(Client, verbose_name='Клиенты', )
    massage = models.ManyToManyField(Massage, verbose_name='Письма', )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE,
                             verbose_name='Пользователь')

    def __str__(self):
        return f'{self.time}, {self.frequency}, {self.status}'

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'
