import pytest
from rest_framework import status
from rest_framework.reverse import reverse


@pytest.mark.django_db
class TestHabitViewSet:
    def test_list_habits(self, authenticated_client, habit):
        url = reverse('habit-list')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] >= 1

    def test_create_habit(self, authenticated_client):
        url = reverse('habit-list')
        data = {
            'place': 'Дома',
            'time': '08:00',
            'action': 'Зарядка',
            'periodicity': 'daily',
            'execution_time': 60
        }
        response = authenticated_client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_delete_own_habit(self, authenticated_client, habit):
        url = reverse('habit-detail', kwargs={'pk': habit.id})
        response = authenticated_client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_public_habits_list(self, authenticated_client, habit):
        habit.is_public = True
        habit.save()

        url = reverse('public-habits')
        response = authenticated_client.get(url)
        assert response.status_code == status.HTTP_200_OK