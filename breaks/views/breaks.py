import pdb

from django.db.models import Q
from drf_spectacular.utils import extend_schema_view, extend_schema
from rest_framework.generics import get_object_or_404

from breaks.models.breaks import Break
from common.views.mixins import ExtendedCRUAPIView
from breaks.serializers.api import breaks as breaks_s


@extend_schema_view(
    get=extend_schema(summary='Деталка репетиции', tags=['Репетиции: Репетиции пользователя']),
    post=extend_schema(summary='Резерв репетиции', tags=['Репетиции: Репетиции пользователя']),
    patch=extend_schema(summary='Измемение резерва репетиции', tags=['Репетиции: Репетиции пользователя']),
)
class BreakMeView(ExtendedCRUAPIView):
    queryset = Break.objects.all()
    serializer_class = breaks_s.BreakMeRetrieveSerializer
    multi_serializer_class = {
        'GET': breaks_s.BreakMeRetrieveSerializer,
        'POST': breaks_s.BreakMeCreateSerializer,
        'PATCH': breaks_s.BreakMeUpdateSerializer,
    }
    http_method_names = ('get', 'post', 'patch')

    def get_object(self):
        user = self.request.user
        replacement_id = self.request.parser_context['kwargs'].get('pk')

        return get_object_or_404(
            Break, Q(replacement_id=replacement_id, member__member__participant__user=user)
        )
