import pytest
from rest_framework.test import APIClient
from users.models import User
from habits.models import Habit


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        email='test@example.com',
        password='testpass123'
    )


@pytest.fixture
def authenticated_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


@pytest.fixture
def habit(user, db):
    return Habit.objects.create(
        owner=user,
        place='Дома',
        time='08:00',
        action='Зарядка',
        periodicity='daily',
        execution_time=60
    )