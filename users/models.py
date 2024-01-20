from django.contrib.auth.models import AbstractUser
from django.db import models
#from main.models import Client

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    #client = models.ManyToManyField(Client, verbose_name='Клиенты')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
