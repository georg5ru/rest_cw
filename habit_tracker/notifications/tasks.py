from celery import shared_task
from django.utils import timezone
from habits.models import Habit
from .telegram_bot import TelegramBot


@shared_task
def send_habit_reminders():
    """Задача для отправки напоминаний о привычках"""
    bot = TelegramBot()
    now = timezone.now()
    current_hour = now.hour
    current_minute = now.minute

    habits = Habit.objects.filter(
        time__hour=current_hour,
        time__minute__lte=current_minute,
        owner__telegram_id__isnull=False
    ).select_related('owner')

    sent_count = 0
    for habit in habits:
        if bot.send_habit_reminder(habit.owner, habit):
            sent_count += 1

    return f'Sent {sent_count} reminders'