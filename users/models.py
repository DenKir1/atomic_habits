from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'blank': True, 'null': True}
ACTIVE_CHOICES = [
    (True, 'Активен'),
    (False, 'Неактивен'),
]


class User(AbstractUser):
    """Модель пользователя"""
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    avatar = models.ImageField(upload_to='user/', verbose_name='Аватар', **NULLABLE)
    is_active = models.BooleanField(default=True, choices=ACTIVE_CHOICES, verbose_name='Почта активирована')
    telegram = models.CharField(max_length=50, verbose_name='Telegram_ID', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.email}'
