from drf_spectacular.utils import extend_schema_view, extend_schema

from common.views.mixins import DictListMixin
from breaks.models.dicts import ReplacementStatus, BreakStatus


@extend_schema_view(
    list=extend_schema(summary='Список статусов репетиций', tags=['Словари']),
)
class ReplacementStatusView(DictListMixin):
    model = ReplacementStatus


@extend_schema_view(
    list=extend_schema(summary='Список статусов репетиций', tags=['Словари']),
)
class BreakStatusView(DictListMixin):
    model = BreakStatus
