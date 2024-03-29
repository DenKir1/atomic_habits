# Generated by Django 4.2.10 on 2024-03-09 08:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=150, verbose_name='Место')),
                ('time', models.TimeField(verbose_name='Время')),
                ('action', models.CharField(max_length=50, verbose_name='Действие')),
                ('duration', models.SmallIntegerField(verbose_name='Продолжительность в минутах')),
                ('is_daily', models.BooleanField(choices=[(True, 'Ежедневная'), (False, 'Еженедельная')], default=False, verbose_name='Периодичность')),
                ('is_good', models.BooleanField(choices=[(True, 'Приятная'), (False, 'Нет')], default=False, verbose_name='Приятная')),
                ('is_public', models.BooleanField(choices=[(True, 'Публичная'), (False, 'Нет')], default=True, verbose_name='Публичная')),
                ('prize', models.CharField(blank=True, max_length=100, null=True, verbose_name='Вознаграждение')),
                ('related', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='habits.habit', verbose_name='Связанная с')),
            ],
            options={
                'verbose_name': 'привычка',
                'verbose_name_plural': 'привычки',
                'ordering': ('id',),
            },
        ),
    ]
