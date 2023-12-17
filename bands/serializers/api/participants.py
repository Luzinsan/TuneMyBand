from crum import get_current_user
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializer
from bands.constants import DIRECTOR_POSITION, OPERATOR_POSITION, \
    MANAGER_POSITION
from bands.models.dicts import Position
from bands.models.bands import Participant, Band
from bands.serializers.nested.dicts import PositionShortSerializer
from users.serializers.nested.users import UserParticipantSerializer

User = get_user_model()


class ParticipantSearchSerializer(ExtendedModelSerializer):
    user = UserParticipantSerializer()
    position = PositionShortSerializer()

    class Meta:
        model = Participant
        fields = (
            'id',
            'position',
            'user',
        )


class ParticipantListSerializer(ExtendedModelSerializer):
    user = UserParticipantSerializer()
    position = PositionShortSerializer()

    class Meta:
        model = Participant
        fields = (
            'id',
            'date_joined',
            'user',
            'position',
        )


class ParticipantRetrieveSerializer(ExtendedModelSerializer):
    user = UserParticipantSerializer()
    position = PositionShortSerializer()

    class Meta:
        model = Participant
        fields = (
            'id',
            'date_joined',
            'user',
            'position',
        )


class ParticipantCreateSerializer(ExtendedModelSerializer):
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Participant
        fields = (
            'id',
            'first_name',
            'last_name',
            'email',
            'password',
            'position',
        )

    def validate(self, attrs):
        current_user = get_current_user()

        band_id = self.context['view'].kwargs.get('pk')
        band = Band.objects.filter(
            id=band_id, leader=current_user,
        ).first()

        # Проверка, что пользователь - руководитель музыкального коллектива
        if not band:
            raise ParseError(
                'Такого коллетива не найдено.'
            )

        attrs['band'] = band

        return attrs

    def create(self, validated_data):
        user_data = {
            'first_name': validated_data.pop('first_name'),
            'last_name': validated_data.pop('last_name'),
            'email': validated_data.pop('email'),
            'password': validated_data.pop('password'),
            'is_corporate_account': True,
        }

        with transaction.atomic():
            user = User.objects.create_user(**user_data)
            validated_data['user'] = user

            instance = super().create(validated_data)
        return instance


class ParticipantUpdateSerializer(ExtendedModelSerializer):
    position = serializers.PrimaryKeyRelatedField(
        queryset=Position.objects.filter(is_active=True)
    )

    class Meta:
        model = Participant
        fields = (
            'position',
        )

    def validate(self, attrs):
        if self.instance.is_leader:
            raise ParseError(
                'Руководитель коллектива недоступен для изменений.'
            )
        return attrs

    def validate_position(self, value):
        if value.code == OPERATOR_POSITION:
            if self.instance.is_manager:
                participant_groups = self.instance.groups_managers.values_list('name', flat=True)
                if participant_groups:
                    error_group_text = ', '.join(participant_groups)
                    raise ParseError(
                        f'Невозможно сменить должность. Участник является '
                        f'менеджером в следующих группах:  {error_group_text}.'
                    )
        return value


class ParticipantDeleteSerializer(serializers.Serializer):
    def validate(self, attrs):
        if self.instance.is_leader:
            raise ParseError(
                'невозможно удалить руководителя из коллектива.'
            )
        groups_as_member = self.instance.groups_members.values_list('name', flat=True)
        groups_as_manager = self.instance.groups_managers.values_list('name', flat=True)
        groups_exists = set(groups_as_member).union(set(groups_as_manager))
        if groups_exists:
            error_group_text = ', '.join(list(groups_exists))
            raise ParseError(
                f'Удаление невозможно. Участник является '
                f'менеджером в следующих группах:  {error_group_text}.'
            )

        return attrs
