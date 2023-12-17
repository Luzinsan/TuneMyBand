from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from common.views.mixins import LCRUDViewSet, ListViewSet
from bands.backends import OwnedByBand
from bands.filters import ParticipantFilter
from bands.models.bands import Participant
from bands.permissions import IsColleagues
from bands.serializers.api import participants as participants_s


@extend_schema_view(
    list=extend_schema(summary='Список участников коллектива', tags=['Коллективы: Участники']),
    retrieve=extend_schema(summary='Деталка участника коллектива', tags=['Коллективы: Участники']),
    create=extend_schema(summary='Создать участника коллектива', tags=['Коллективы: Участники']),
    update=extend_schema(summary='Изменить участника коллектива', tags=['Коллективы: Участники']),
    partial_update=extend_schema(summary='Изменить участника коллектива частично', tags=['Коллективы: Участники']),
    destroy=extend_schema(summary='Удалить участника из коллектива', tags=['Коллективы: Участники']),
    search=extend_schema(filters=True, summary='Список участников коллектива Search', tags=['Словари']),
)
class ParticipantView(LCRUDViewSet):
    permission_classes = [IsColleagues]

    queryset = Participant.objects.all()
    serializer_class = participants_s.ParticipantListSerializer

    multi_serializer_class = {
        'list': participants_s.ParticipantListSerializer,
        'retrieve': participants_s.ParticipantRetrieveSerializer,
        'create': participants_s.ParticipantCreateSerializer,
        'update': participants_s.ParticipantUpdateSerializer,
        'partial_update': participants_s.ParticipantUpdateSerializer,
        'search': participants_s.ParticipantSearchSerializer,
        'destroy': participants_s.ParticipantDeleteSerializer,
    }

    lookup_url_kwarg = 'participant_id'
    http_method_names = ('get', 'post', 'patch', 'delete',)

    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
        SearchFilter,
        OwnedByBand,
    )
    filterset_class = ParticipantFilter
    ordering = ('position', 'date_joined', 'id',)

    def get_queryset(self):
        qs = Participant.objects.select_related(
            'user',
            'position',
        ).prefetch_related(
            'band',
        )
        return qs

    @action(methods=['GET'], detail=False, url_path='search')
    def search(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=dict())
        serializer.is_valid(raise_exception=True)
        return super().destroy(request, *args, **kwargs)
