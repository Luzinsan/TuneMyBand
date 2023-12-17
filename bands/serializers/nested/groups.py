from common.serializers.mixins import ExtendedModelSerializer
from bands.models.groups import Group
from bands.serializers.nested.participants import ParticipantsShortSerializer
from bands.serializers.nested.bands import \
    BandShortSerializer


class GroupShortSerializer(ExtendedModelSerializer):
    band = BandShortSerializer()
    manager = ParticipantsShortSerializer()

    class Meta:
        model = Group
        fields = (
            'id',
            'name',
            'band',
            'manager',
        )
