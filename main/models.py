from django.db import models

NULLABLE = {'blank': True, 'null': True}  # шаблон для необязательного элемента


class Settings(models.Model):
    ONES_A_DAY = 'Раз в день'
    ONES_A_WEEK = 'Раз в неделю'
    ONES_A_MONTH = 'Раз в месяц'

    FREQUENCY_TYPES = ((ONES_A_DAY, 'Раз в день'), (ONES_A_WEEK, 'Раз в неделю'), (ONES_A_MONTH, 'Раз в месяц'))

    COMPLETED = 'Завершена'
    CREATED = 'Создана'
    LAUNCHED = 'Запущена'

    STATUS_TYPES = ((COMPLETED, 'Завершена'), (CREATED, 'Создана'), (LAUNCHED, 'Запущена'))

    time = models.TimeField(verbose_name='Время рассылки', default='00:00:00')
    frequency = models.CharField(default=ONES_A_DAY, choices=FREQUENCY_TYPES, verbose_name='Периодичность')
    status = models.CharField(max_length=10, default=CREATED, choices=STATUS_TYPES, verbose_name='Статус')

    def __str__(self):
        return f'{self.time}, {self.frequency}, {self.status}'

    class Meta:
        verbose_name = 'Настройка'
        verbose_name_plural = 'Настройки'


class Logs(models.Model):
    datatime = models.DateTimeField(verbose_name='Время и дата последней попытки', auto_now=True)
    status = models.CharField(max_length=100, verbose_name='Статус попытки')
    response = models.CharField(max_length=100, verbose_name='Ответ сервера', )

    def __str__(self):
        return f'{self.status}, {self.response}, {self.datatime}'

    class Meta:
        verbose_name = 'Логи'
        verbose_name_plural = 'Логи'


class Client(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя', **NULLABLE)
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', **NULLABLE)
    sur_name = models.CharField(max_length=150, verbose_name='Отчество', **NULLABLE)
    mail = models.EmailField(unique=True, verbose_name='Почта')
    description = models.TextField(verbose_name='Описание', **NULLABLE)

    def __str__(self):
        return f'{self.mail}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class Massage(models.Model):
    head = models.CharField(max_length=150, verbose_name='Тема письма')
    body = models.TextField(verbose_name='Тело письма')

    settings = models.ForeignKey(Settings, on_delete=models.CASCADE, verbose_name='Настройки', **NULLABLE)
    logs = models.ForeignKey(Logs, on_delete=models.CASCADE, verbose_name='Логи', **NULLABLE)
    client = models.ManyToManyField(Client, verbose_name='Клиенты',)

    def __str__(self):
        return f'{self.head}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
