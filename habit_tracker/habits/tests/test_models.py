import pytest
from django.core.exceptions import ValidationError
from habits.models import Habit


@pytest.mark.django_db
class TestHabitModel:
    def test_habit_creation(self, user):
        habit = Habit.objects.create(
            owner=user,
            place='Дома',
            time='08:00',
            action='Зарядка',
            periodicity='daily'
        )
        assert habit.action == 'Зарядка'
        assert habit.owner == user

    def test_execution_time_validator(self, user):
        with pytest.raises(ValidationError):
            habit = Habit(
                owner=user,
                place='Дома',
                time='08:00',
                action='Зарядка',
                execution_time=150
            )
            habit.full_clean()

    def test_reward_and_related_habit_validator(self, user):
        pleasant_habit = Habit.objects.create(
            owner=user,
            place='Дома',
            time='08:00',
            action='Ванна',
            is_pleasant=True
        )

        with pytest.raises(ValidationError):
            habit = Habit(
                owner=user,
                place='Дома',
                time='08:00',
                action='Зарядка',
                reward='Вкусный завтрак',
                related_habit=pleasant_habit
            )
            habit.full_clean()