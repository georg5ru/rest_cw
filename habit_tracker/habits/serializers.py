from rest_framework import serializers
from .models import Habit
from .validators import HabitRewardValidator


class HabitSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Habit
        fields = [
            'id', 'owner', 'place', 'time', 'action', 'is_pleasant',
            'related_habit', 'periodicity', 'reward', 'execution_time',
            'is_public', 'created_at', 'updated_at'
        ]
        read_only_fields = ['owner', 'created_at', 'updated_at']

    def validate(self, data):
        habit = Habit(**data)
        HabitRewardValidator()(habit)
        return data

    def create(self, validated_data):
        validated_data['owner'] = self.context['request'].user
        return super().create(validated_data)


class PublicHabitSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Habit
        fields = [
            'id', 'owner', 'place', 'time', 'action', 'is_pleasant',
            'periodicity', 'execution_time', 'is_public'
        ]