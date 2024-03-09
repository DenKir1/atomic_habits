from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework import status
from habits.models import Habit
from users.models import User


class HabitListTestCase(APITestCase):
    maxDiff = None

    def setUp(self) -> None:

        self.user = User.objects.create(
            email='test@test.test',
            telegram='test'
        )

        self.private_habit = Habit.objects.create(
            user=self.user,
            place="test",
            time="12:00",
            action="test",
            duration=2,
            prize="test"
        )

        self.public_habit = Habit.objects.create(
            user=self.user,
            place="test",
            time="12:00",
            action="test",
            duration=2,
            prize="test",
            is_public=True
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_get_habits_list(self):
        """Тестирование вывода списка привычек"""

        response = self.client.get(reverse('habits:habit_list'))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_habit(self):
        """Тестирование вывода одной привычки"""

        response = self.client.get(reverse('habits:habit_detail', kwargs={'pk': self.private_habit.id}))

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_public_habits_list(self):
        """Тестирование вывода списка публичных привычек"""

        response = self.client.get(reverse('habits:habit_public_list'))
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class HabitUpdateTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.test',
            telegram='test'
        )

        self.habit = Habit.objects.create(
            user=self.user,
            place="test",
            time="12:00",
            action="test",
            duration=2,
            prize="test"
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_patch_habit(self):
        """Тестирование обновления """

        changed_data = {
            "place": "test2",
        }

        response = self.client.patch(
            reverse('habits:habit_update', kwargs={'pk': self.habit.id}),
            data=changed_data)
        self.maxDiff = None

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )


class HabitDestroyTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(
            email='test@test.test',
            telegram='test'
        )

        self.habit = Habit.objects.create(
            user=self.user,
            place="test",
            time="12:00",
            action="test",
            duration=2,
            prize="test"
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_delete_habit(self):
        """Тестирование удаления """

        response = self.client.delete(
            reverse('habits:habit_delete', kwargs={'pk': self.habit.pk}))
        self.maxDiff = None
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
