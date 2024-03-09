from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self) -> None:
        self.user = User.objects.create(email='test@test.com')
        self.user.set_password('test')
        self.user.save()

        self.client.force_authenticate(user=self.user)

    def test_create_habit(self):
        """ Create test """
        response = self.client.post('/users/token/', {"email": "test@test.com", "password": "12345"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        data_habit = {
            'user': self.user.pk,
            'place': 'Test',
            'time': '00:00',
            'action': 'Test',
            'duration': 'Test',
            'is_good': True,
            'is_daily': True,
        }

        response = self.client.post(
            '/habits/habit_create/',
            data=data_habit
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habit(self):
        """ List test """
        response = self.client.post('/users/token/', {"email": "test@test.com", "password": "12345"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')
        response = self.client.get(
            '/habits/'
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_detail_habit(self):
        """  Detail test  """
        response = self.client.post('/users/token/', {"email": "test@test.com", "password": "12345"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        habit = Habit.objects.create(
            user=self.user.pk,
            place='Test',
            time='00:00',
            action='Test',
            duration='Test',
            is_good=True,
            is_daily=True,
        )

        response = self.client.get(
            reverse('habits:habit_detail', kwargs={'pk': habit.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_change_habit(self):
        """ Change test """

        response = self.client.post('/users/token/', {"email": "test@test.com", "password": "12345"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        habit = Habit.objects.create(
            user=self.user.pk,
            place='Test',
            time='00:00',
            action='Test',
            duration='Test',
            is_good=True,
            is_daily=True,
        )

        habit_change = {
            'place': 'Test_1',
        }

        response = self.client.patch(
            reverse('habits:habit_change', kwargs={'pk': habit.pk}),
            data=habit_change
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habit(self):
        """ Delete test """
        response = self.client.post('/users/token/', {"email": "test@test.com", "password": "12345"})
        self.access_token = response.json().get("access")
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

        habit = Habit.objects.create(
            user=self.user.pk,
            place='Test',
            time='00:00',
            action='Test',
            duration='Test',
            is_good=True,
            is_daily=True,
        )

        response = self.client.delete(
            reverse('habits:habit_delete', kwargs={'pk': habit.pk})
        )

        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
