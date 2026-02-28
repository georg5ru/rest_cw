import requests
from django.conf import settings


class TelegramBot:
    """Класс для работы с Telegram Bot API"""

    def __init__(self):
        self.token = settings.TELEGRAM_BOT_TOKEN
        self.base_url = f'https://api.telegram.org/bot{self.token}'

    def send_message(self, chat_id, text):
        """Отправка сообщения пользователю"""
        url = f'{self.base_url}/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': text,
            'parse_mode': 'HTML'
        }
        try:
            response = requests.post(url, json=data, timeout=10)
            return response.status_code == 200
        except Exception as e:
            print(f'Error sending Telegram message: {e}')
            return False

    def send_habit_reminder(self, user, habit):
        """Отправка напоминания о привычке"""
        if not user.telegram_id:
            return False

        text = f"""
🔔 <b>Напоминание о привычке!</b>

📍 <b>Место:</b> {habit.place}
⏰ <b>Время:</b> {habit.time}
✅ <b>Действие:</b> {habit.action}
⏱ <b>Время на выполнение:</b> {habit.execution_time} сек

Не забудьте вознаградить себя! 🎁
        """
        return self.send_message(user.telegram_id, text)