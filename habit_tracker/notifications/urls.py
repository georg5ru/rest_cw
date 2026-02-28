from django.urls import path
from .views import SetTelegramIdView

urlpatterns = [
    path('set-telegram-id/', SetTelegramIdView.as_view(), name='set-telegram-id'),
]