from common.serializers.mixins import ExtendedModelSerializer
from bands.models.bands import Band


class BandShortSerializer(ExtendedModelSerializer):
    class Meta:
        model = Band
        fields = (
            'id',
            'name',
        )
