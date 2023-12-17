from crum import get_current_user
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ParseError

from common.serializers.mixins import ExtendedModelSerializer, \
    InfoModelSerializer
from bands.constants import DIRECTOR_POSITION
from bands.models.bands import Band
from users.serializers.nested.users import UserShortSerializer


User = get_user_model()


class BandSearchListSerializer(ExtendedModelSerializer):
    leader = UserShortSerializer()

    class Meta:
        model = Band
        fields = (
            'id',
            'name',
            'leader',
        )


class BandListSerializer(InfoModelSerializer):
    leader = UserShortSerializer()
    pax = serializers.IntegerField()
    groups_count = serializers.IntegerField()
    can_manage = serializers.BooleanField()

    class Meta:
        model = Band
        fields = (
            'id',
            'name',
            'leader',
            'pax',
            'groups_count',
            'created_at',
            'can_manage',
        )


class BandRetrieveSerializer(InfoModelSerializer):
    leader = UserShortSerializer()
    pax = serializers.IntegerField()
    groups_count = serializers.IntegerField()
    can_manage = serializers.BooleanField()

    class Meta:
        model = Band
        fields = (
            'id',
            'name',
            'leader',
            'pax',
            'groups_count',
            'created_at',
            'can_manage',
        )


class BandCreateSerializer(ExtendedModelSerializer):
    class Meta:
        model = Band
        fields = (
            'id',
            'name',
        )

    def validate_name(self, value):
        if self.Meta.model.objects.filter(name=value):
            raise ParseError(
                'Коллектив с таким названием уже существует'
            )
        return value

    def validate(self, attrs):
        user = get_current_user()
        attrs['leader'] = user
        return attrs

    def create(self, validated_data):
        with transaction.atomic():
            instance = super().create(validated_data)
            instance.participants.add(
                validated_data['leader'],
                through_defaults={'position_id': DIRECTOR_POSITION, }
            )
        return instance


class BandUpdateSerializer(ExtendedModelSerializer):
    class Meta:
        model = Band
        fields = (
            'id',
            'name',
        )
