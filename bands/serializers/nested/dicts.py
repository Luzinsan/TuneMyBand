from common.serializers.mixins import DictMixinSerializer
from bands.models.dicts import Position


class PositionShortSerializer(DictMixinSerializer):
    class Meta:
        model = Position
