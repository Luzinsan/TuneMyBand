from django.db.models import Count, Case, When, Q
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter

from common.views.mixins import LCRUViewSet
from bands.backends import MyBand, MyGroup
from bands.filters import GroupFilter
from bands.models.groups import Group
from bands.permissions import IsColleagues, IsMyGroup
from bands.serializers.api import groups as groups_s


@extend_schema_view(
    list=extend_schema(summary='Список групп', tags=['Музыкальные коллективы: Группы']),
    retrieve=extend_schema(summary='Деталка группы', tags=['Музыкальные коллективы: Группы']),
    create=extend_schema(summary='Создать группу', tags=['Музыкальные коллективы: Группы']),
    update=extend_schema(summary='Изменить группу', tags=['Музыкальные коллективы: Группы']),
    partial_update=extend_schema(summary='Изменить группу частично', tags=['Музыкальные коллективы: Группы']),
    update_settings=extend_schema(summary='Изменить настройки группы', tags=['Музыкальные коллективы: Группы']),
)
class GroupView(LCRUViewSet):
    permission_classes = [IsMyGroup]

    queryset = Group.objects.all()
    serializer_class = groups_s.GroupListSerializer

    multi_serializer_class = {
        'list': groups_s.GroupListSerializer,
        'retrieve': groups_s.GroupRetrieveSerializer,
        'create': groups_s.GroupCreateSerializer,
        'update': groups_s.GroupUpdateSerializer,
        'partial_update': groups_s.GroupUpdateSerializer,
        'update_settings': groups_s.GroupSettingsUpdateSerializer,
    }

    http_method_names = ('get', 'post', 'patch')

    filter_backends = (
        OrderingFilter,
        SearchFilter,
        DjangoFilterBackend,
        MyGroup,
    )
    search_fields = ('name',)
    filterset_class = GroupFilter
    ordering = ('name', 'id',)

    def get_queryset(self):
        queryset = Group.objects.select_related(
            'manager',
        ).prefetch_related(
            'band',
            'band__leader',
            'members',
        ).annotate(
            pax=Count('members', distinct=True),
            can_manage=Case(
                When(
                    Q(manager__user=self.request.user) |
                    Q(band__leader=self.request.user),
                    then=True
                ),
                default=False,
            ),
            _is_member_count=Count(
                'members', filter=(Q(members__user=self.request.user)), distinct=True,
            ),
            is_member=Case(
                When(Q(_is_member_count__gt=0), then=True), default=False,
            ),

        )
        return queryset

    @action(methods=['PATCH'], detail=True, url_path='settings')
    def update_settings(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)