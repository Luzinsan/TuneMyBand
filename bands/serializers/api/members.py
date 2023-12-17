from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializer

from bands.models.groups import Member, Group
from bands.models.bands import Participant
from bands.serializers.nested.dicts import PositionShortSerializer
from bands.serializers.nested.participants import ParticipantsShortSerializer

User = get_user_model()


class MemberSearchSerializer(ExtendedModelSerializer):
    full_name = serializers.CharField(source='participant.user.full_name')
    username = serializers.CharField(source='participant.user.username')
    position = PositionShortSerializer(source='participant.position')

    class Meta:
        model = Member
        fields = (
            'id',
            'full_name',
            'username',
            'position',
        )


class MemberListSerializer(ExtendedModelSerializer):
    participant = ParticipantsShortSerializer()

    class Meta:
        model = Member
        fields = (
            'id',
            'participant',
            'date_joined',
        )


class MemberRetrieveSerializer(ExtendedModelSerializer):
    participant = ParticipantsShortSerializer()

    class Meta:
        model = Member
        fields = (
            'id',
            'participant',
            'date_joined',
        )


class MemberCreateSerializer(ExtendedModelSerializer):
    participants = serializers.PrimaryKeyRelatedField(
        queryset=Participant.objects.all(), many=True, write_only=True
    )

    class Meta:
        model = Member
        fields = (
            'id',
            'participants',
        )

    def validate(self, attrs):
        try:
            group = self.get_object_from_url(Group)
            band = group.band
        except:
            raise ParseError('Ой, что-то не так. Текущий коллектив не найден.')

        attrs['group'] = group

        participants = attrs['participants']
        participants_id_set = {obj.pk for obj in participants}

        org_participants = band.participants_info.all()
        org_participants_id_set = {obj.pk for obj in org_participants}

        # Check participants from request exist in org
        if participants_id_set - org_participants_id_set:
            raise ParseError(
                'Некоторые из указанных участников не существуют в коллективе. '
                'Проверьте введенные данные.'
            )

        return attrs

    def create(self, validated_data):
        participants = validated_data.pop('participants')
        group = validated_data.pop('group')
        group.members.set(participants)
        return group
