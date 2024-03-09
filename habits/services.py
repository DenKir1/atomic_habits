from django_celery_beat.models import CrontabSchedule

from config import settings
from django.http import HttpResponse
from django_celery_beat.models import PeriodicTask

from datetime import datetime

import pytz

from habits.models import Habit
from habits.tasks import send_message_from_bot


def check_habits_daily():
    """ Проверка ежедневных привычек на выполнение """

    date_time_now = datetime.now()
    moscow_timezone = pytz.timezone('Europe/Moscow')
    date_now = date_time_now.astimezone(moscow_timezone)
    time_now = date_now.time()

    habits = Habit.objects.filter(time__hour=time_now.hour, time__minute=time_now.minute,
                                  is_daily=True, is_good=False)

    for habit in habits:
        create_message(habit.id)


def check_habits_weekly():
    """ Проверка еженедельных привычек на выполнение """

    date_time_now = datetime.now()
    moscow_timezone = pytz.timezone('Europe/Moscow')
    date_now = date_time_now.astimezone(moscow_timezone)
    time_now = date_now.time()

    habits = Habit.objects.filter(time__hour=time_now.hour, time__minute=time_now.minute,
                                  is_daily=False, is_good=False)

    for habit in habits:
        create_message(habit.id)


def create_message(habit_id):
    """ Функция создания сообщения для отправки в телеграм-бот """

    habit = Habit.objects.get(id=habit_id)
    response = send_message_from_bot(habit_id)
    if habit.related:
        habit_prize = Habit.objects.get(id=habit.related.id)
        nice_response = send_message_from_bot(habit_prize.id)
        return HttpResponse(nice_response)
    return HttpResponse(response)


def create_task(habit):
    """ Создание расписания и задачи """

    crontab_schedule, _ = CrontabSchedule.objects.get_or_create(
        minute=habit.time.minute,
        hour=habit.time.hour,
        day_of_week='*' if habit.is_daily else '*/7',
        month_of_year='*',
        timezone=settings.TIME_ZONE
    )

    PeriodicTask.objects.create(
        crontab=crontab_schedule,
        name=f'Habit Task - {habit.id}',
        task='habits.tasks.send_message_from_bot',
        args=[habit.id],
    )


def delete_task(habit):
    """ Удаление задачи """

    task_name = f'send_message_from_bot_{habit.id}'
    PeriodicTask.objects.filter(name=task_name).delete()


def update_task(habit):
    """ Обновление задачи """

    delete_task(habit)
    create_task(habit)
