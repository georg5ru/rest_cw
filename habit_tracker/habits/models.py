from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from .validators import HabitTimeValidator, HabitRewardValidator


class Habit(models.Model):
    """Модель привычки"""

    PERIODICITY_CHOICES = [
        ('daily', 'Ежедневно'),
        ('weekly', 'Еженедельно'),
        ('monthly', 'Ежемесячно'),
    ]

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='habits',
        verbose_name='Владелец'
    )
    place = models.CharField('Место', max_length=200)
    time = models.TimeField('Время')
    action = models.CharField('Действие', max_length=200)
    is_pleasant = models.BooleanField('Приятная привычка', default=False)
    related_habit = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='related_habits',
        verbose_name='Связанная привычка',
        limit_choices_to={'is_pleasant': True}
    )
    periodicity = models.CharField(
        'Периодичность',
        max_length=20,
        choices=PERIODICITY_CHOICES,
        default='daily'
    )
    reward = models.CharField('Вознаграждение', max_length=200, blank=True, null=True)
    execution_time = models.IntegerField(
        'Время на выполнение (секунды)',
        validators=[HabitTimeValidator()],
        default=120
    )
    is_public = models.BooleanField('Публичная', default=False)
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.action} ({self.owner.email})"

    def clean(self):
        super().clean()
        HabitRewardValidator()(self)

        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError({
                'related_habit': 'Связанная привычка должна быть приятной'
            })