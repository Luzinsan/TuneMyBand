from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.decorators import action

from common.views.mixins import LCDViewSet
from bands.backends import OwnedByGroup
from bands.models.groups import Member
from bands.permissions import IsColleagues
from bands.serializers.api import members as members_s


@extend_schema_view(
    list=extend_schema(summary='Список участников группы', tags=['Музыкальные коллективы: Группы: Участники']),
    create=extend_schema(summary='Создать участника группы', tags=['Музыкальные коллективы: Группы: Участники']),
    destroy=extend_schema(summary='Удалить участника из группы', tags=['Музыкальные коллективы: Группы: Участники']),
    search=extend_schema(filters=True, summary='Список участников группы Search', tags=['Словари']),
)
class MemberView(LCDViewSet):
    permission_classes = [IsColleagues]

    queryset = Member.objects.all()
    serializer_class = members_s.MemberListSerializer

    multi_serializer_class = {
        'list': members_s.MemberListSerializer,
        'create': members_s.MemberCreateSerializer,
        'search': members_s.MemberSearchSerializer,
    }

    lookup_url_kwarg = 'member_id'

    filter_backends = (OwnedByGroup,)

    def get_queryset(self):
        qs = Member.objects.select_related(
            'participant',
        ).prefetch_related(
            'group',
            'participant__user',
            'participant__band',
            'participant__band',
            'participant__position',
        )
        return qs

    @action(methods=['GET'], detail=False, url_path='search')
    def search(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
