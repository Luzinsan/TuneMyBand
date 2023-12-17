from crum import get_current_user
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.filters import OrderingFilter
from rest_framework.generics import get_object_or_404

from breaks.factory.replacements import ReplacementFactory
from breaks.models.replacements import Replacement, ReplacementMember
from common.views.mixins import LCRUViewSet, ExtendedRetrieveUpdateAPIView
from breaks.serializers.api import replacements as replacements_s


@extend_schema_view(
    list=extend_schema(summary='Список репетиционных дней', tags=['Репетиции: Репетиционные дни']),
    retrieve=extend_schema(summary='Деталка репетиционного дня', tags=['Репетиции: Репетиционные дни']),
    create=extend_schema(summary='Создать репетиционный день', tags=['Репетиции: Репетиционные дни']),
    partial_update=extend_schema(summary='Изменить репетиционный день частично', tags=['Репетиции: Репетиционные дни']),
)
class ReplacementView(LCRUViewSet):

    queryset = Replacement.objects.all()
    serializer_class = replacements_s.ReplacementListSerializer

    multi_serializer_class = {
        'list': replacements_s.ReplacementListSerializer,
        'retrieve': replacements_s.ReplacementRetrieveSerializer,
        'create': replacements_s.ReplacementCreateSerializer,
        'partial_update': replacements_s.ReplacementUpdateSerializer,
    }

    http_method_names = ('get', 'post', 'patch')

    filter_backends = (
        OrderingFilter,
        DjangoFilterBackend,
        # MyReplacement,
    )
    # filterset_class = ReplacementFilter

    def get_queryset(self):
        return ReplacementFactory().list()


@extend_schema_view(
    get=extend_schema(summary='Данные участника репетиции', tags=['Репетиции: Репетиционные дни']),
    patch=extend_schema(summary='Изменить участника репетиции', tags=['Репетиции: Репетиционные дни']),
)
class MeReplacementMemberView(ExtendedRetrieveUpdateAPIView):
    queryset = ReplacementMember.objects.all()
    serializer_class = replacements_s.ReplacementMemberListSerializer
    multi_serializer_class = {
        'GET': replacements_s.ReplacementMemberListSerializer,
        'PATCH': replacements_s.ReplacementMemberUpdateSerializer,
    }

    def get_object(self):
        user = get_current_user()
        replacement_id = self.request.parser_context['kwargs'].get('pk')
        member = get_object_or_404(
            ReplacementMember,
            Q(replacement_id=replacement_id, member__participant__user=user)
        )
        return member
