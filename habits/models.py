from django.conf import settings
from django.db import models

from users.models import NULLABLE

PERIOD_CHOICES = (
        (True, 'Ежедневная'),
        (False, 'Еженедельная'),
    )

IS_GOOD_CHOICES = (
        (True, 'Приятная'),
        (False, 'Нет'),
    )

PUBLIC_CHOICES = (
        (True, 'Публичная'),
        (False, 'Нет'),
    )


class Habit(models.Model):
    """Модель - привычка"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Владелец', **NULLABLE)
    place = models.CharField(max_length=150, verbose_name='Место')
    time = models.TimeField(verbose_name='Время')
    action = models.CharField(max_length=50, verbose_name='Действие')
    duration = models.SmallIntegerField(verbose_name='Продолжительность в минутах')
    is_daily = models.BooleanField(default=False, choices=PERIOD_CHOICES, verbose_name='Периодичность')
    is_good = models.BooleanField(default=False, verbose_name='Приятная', choices=IS_GOOD_CHOICES)
    is_public = models.BooleanField(default=True, verbose_name='Публичная', choices=PUBLIC_CHOICES)
    related = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='Связанная с', **NULLABLE)
    prize = models.CharField(max_length=100, verbose_name='Вознаграждение', **NULLABLE)

    def __str__(self):
        return f'{self.place} - {self.time} - {self.action}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'
        ordering = ('id',)
