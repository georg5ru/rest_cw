from django.core.exceptions import ValidationError


class HabitTimeValidator:
    """Валидатор времени выполнения (не больше 120 секунд)"""

    def __call__(self, value):
        if value > 120:
            raise ValidationError('Время выполнения не должно превышать 120 секунд')
        if value < 1:
            raise ValidationError('Время выполнения должно быть больше 0')


class HabitRewardValidator:
    """Валидатор вознаграждения и связанной привычки"""

    def __call__(self, habit):
        if habit.reward and habit.related_habit:
            raise ValidationError(
                'Нельзя указать одновременно вознаграждение и связанную привычку'
            )

        if habit.is_pleasant:
            if habit.reward:
                raise ValidationError('У приятной привычки не может быть вознаграждения')
            if habit.related_habit:
                raise ValidationError('У приятной привычки не может быть связанной привычки')