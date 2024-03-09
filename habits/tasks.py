import requests
from celery import shared_task

from config.settings import TELEGRAM_URL, TELEGRAM_TOKEN
from habits.models import Habit


@shared_task
def send_message_from_bot(habit_id):
    """ Отправка сообщения в Телеграм"""
    habit = Habit.objects.get(id=habit_id)
    requests.get(
        url=f'{TELEGRAM_URL}{TELEGRAM_TOKEN}/sendMessage',
        params={
            'chat_id': habit.user.telegram,
            'text': f"""Привет {habit.user}! Время {habit.time}.
            Иди в {habit.place} и сделай {habit.action}. 
            На все - про все {habit.duration} минут!"""
        }
    )
