from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Habit
from .serializers import HabitSerializer, PublicHabitSerializer
from .permissions import IsOwnerOrReadOnly
from .pagination import CustomPagination


class HabitViewSet(viewsets.ModelViewSet):
    """ViewSet для личных привычек пользователя"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Habit.objects.filter(owner=user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PublicHabitListView(generics.ListAPIView):
    """Список публичных привычек (только чтение)"""
    serializer_class = PublicHabitSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPagination

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)