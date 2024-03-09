from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from habits.models import Habit
from habits.paginators import HabitPaginator
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer
from habits.services import create_task, update_task, delete_task


class HabitCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        """ Определяем порядок создания нового объекта """

        new_habit = serializer.save()
        new_habit.user = self.request.user
        create_task(new_habit)
        new_habit.save()


class HabitListAPIView(generics.ListAPIView):
    """ Вывод списка привычек пользователя """

    queryset = Habit.objects.all()
    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Habit.objects.filter(user=self.request.user)
        return queryset


class HabitPublicListAPIView(generics.ListAPIView):
    """ Вывод списка публичных привычек """

    serializer_class = HabitSerializer
    pagination_class = HabitPaginator
    permission_classes = [AllowAny]

    def get_queryset(self):
        """ Определяем параметры вывода объектов """

        queryset = Habit.objects.filter(is_public=True)
        return queryset


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Просмотр информации об одной привычке """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Изменение привычки """

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):

        habit = serializer.save()
        update_task(habit)
        habit.save()


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """

    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_destroy(self, instance):
        delete_task(instance)
        instance.delete()
