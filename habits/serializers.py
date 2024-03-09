from rest_framework import serializers

from habits.models import Habit
from habits.validators import validator_habit


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'

        validators = [
            validator_habit,
        ]
