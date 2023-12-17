
from crum import get_current_user
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from breaks.serializers.nested.replacements import BreakSettingsSerializer
from common.serializers.mixins import ExtendedModelSerializer, \
    InfoModelSerializer
from bands.models.groups import Group
from bands.models.bands import Band
from bands.serializers.nested.participants import ParticipantsShortSerializer
from bands.serializers.nested.bands import \
    BandShortSerializer

User = get_user_model()


class GroupListSerializer(InfoModelSerializer):
    band = BandShortSerializer()
    manager = ParticipantsShortSerializer()
    pax = serializers.IntegerField()
    can_manage = serializers.BooleanField()
    is_member = serializers.BooleanField()

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'manager',
            'band',
            'pax',
            'created_at',
            'can_manage',
            'is_member',
        )


class GroupRetrieveSerializer(InfoModelSerializer):
    breaks_info = BreakSettingsSerializer(allow_null=True)
    band = BandShortSerializer()
    manager = ParticipantsShortSerializer()
    pax = serializers.IntegerField()
    can_manage = serializers.BooleanField()
    is_member = serializers.BooleanField()

    class Meta:
        model = Group
        fields = (
            'id',
            'breaks_info',
            'name',
            'band',
            'manager',
            'pax',
            'created_at',
            'can_manage',
            'is_member',
        )


class GroupCreateSerializer(ExtendedModelSerializer):
    class Meta:
        model = Group
        fields = (
            'id',
            'band',
            'manager',
            'name',
        )
        extra_kwargs = {
            'manager': {'required': False, 'allow_null': True, },
        }

    def validate_band(self, value):
        user = get_current_user()
        if value not in Band.objects.filter(leader=user, ):
            return ParseError(
                'Неверно выбран коллектив.'
            )
        return value

    def validate(self, attrs):
        org = attrs['band']

        # Specified manager or band leader
        attrs['manager'] = attrs.get('manager') or org.leader_participant
        manager = attrs['manager']
        # Check manager
        if manager not in org.participants_info.all():
            raise ParseError(
                'Администратором может быть только участник коллектива или руководитель.'
            )

        # Check name duplicate
        if self.Meta.model.objects.filter(
                band=org, name=attrs['name']
        ).exists():
            raise ParseError(
                'Группа с таким названием уже существует.'
            )
        return attrs


class GroupUpdateSerializer(ExtendedModelSerializer):

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'members',
        )

    def validate(self, attrs):
        # Check name duplicate
        if self.instance.band.groups.filter(name=attrs['name']).exists():
            raise ParseError(
                'Группа с таким названием уже существует.'
            )
        return attrs


class GroupSettingsUpdateSerializer(ExtendedModelSerializer):
    breaks_info = BreakSettingsSerializer()

    class Meta:
        model = Group
        fields = (
            'id',
            'breaks_info',
        )

    def update(self, instance, validated_data):
        with transaction.atomic():
            for key, value in validated_data.items():
                self._update_group_profile(key, value)
        return instance

    def _update_group_profile(self, param, validated_data):
        if param in self.fields:
            serializer = self.fields[param]
            instance, c = serializer.Meta.model.objects.get_or_create(
                group_id=self.get_from_url('pk')
            )
            serializer.update(instance, validated_data)
        return
