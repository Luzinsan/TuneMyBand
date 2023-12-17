from crum import get_current_user
from django.db.models import Count, Case, When
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from common.views.mixins import ListViewSet, LCRUViewSet
from bands.backends import MyBand
from bands.filters import BandFilter
from bands.models.bands import Band
from bands.permissions import IsMyBand
from bands.serializers.api import bands


@extend_schema_view(
    list=extend_schema(summary='Список коллективов Search', tags=['Словари']),
)
class BandSearchView(ListViewSet):
    queryset = Band.objects.all()
    serializer_class = bands.BandSearchListSerializer


@extend_schema_view(
    list=extend_schema(summary='Список коллективов', tags=['Коллективы']),
    retrieve=extend_schema(summary='Деталка коллектива', tags=['Коллективы']),
    create=extend_schema(summary='Создать коллектив', tags=['Коллективы']),
    update=extend_schema(summary='Изменить коллектив', tags=['Коллективы']),
    partial_update=extend_schema(summary='Изменить коллектив частично', tags=['Коллективы']),
)
class BandView(LCRUViewSet):
    permission_classes = [IsMyBand]
    queryset = Band.objects.all()
    serializer_class = bands.BandListSerializer

    multi_serializer_class = {
        'list': bands.BandListSerializer,
        'retrieve': bands.BandRetrieveSerializer,
        'create': bands.BandCreateSerializer,
        'update': bands.BandUpdateSerializer,
        'partial_update': bands.BandUpdateSerializer,
    }

    http_method_names = ('get', 'post', 'patch')

    filter_backends = (
        OrderingFilter,
        SearchFilter,
        DjangoFilterBackend,
        MyBand,
    )
    filterset_class = BandFilter
    ordering = ('name', 'id',)

    def get_queryset(self):
        queryset = Band.objects.select_related(
            'leader',
        ).prefetch_related(
            'participants',
            'groups',
        ).annotate(
            pax=Count('participants', distinct=True),
            groups_count=Count('groups', distinct=True),
            can_manage=Case(
                When(leader=self.request.user, then=True),
                default=False,
            )
        )
        return queryset
