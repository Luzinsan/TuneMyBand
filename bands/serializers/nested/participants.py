from common.serializers.mixins import ExtendedModelSerializer
from bands.models.bands import Participant
from bands.serializers.nested.dicts import PositionShortSerializer
from users.serializers.nested.users import UserShortSerializer


class ParticipantsShortSerializer(ExtendedModelSerializer):
    user = UserShortSerializer()
    position = PositionShortSerializer()

    class Meta:
        fields = (
            'id',
            'user',
            'position',
        )
        model = Participant
