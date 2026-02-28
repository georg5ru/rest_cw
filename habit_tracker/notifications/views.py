from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import User


class SetTelegramIdView(generics.UpdateAPIView):
    """Установка Telegram ID пользователя"""
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = request.user
        telegram_id = request.data.get('telegram_id')

        if telegram_id:
            user.telegram_id = telegram_id
            user.save()
            return Response({'message': 'Telegram ID установлен'})

        return Response(
            {'error': 'Telegram ID не указан'},
            status=status.HTTP_400_BAD_REQUEST
        )