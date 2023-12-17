from django.db.models import Q
from rest_framework.filters import BaseFilterBackend


class OwnedByBand(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        org_id = request.parser_context['kwargs'].get('pk')
        return queryset.filter(band_id=org_id)


class OwnedByGroup(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        group_id = request.parser_context['kwargs'].get('pk')
        return queryset.filter(group_id=group_id)


class MyBand(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user
        return queryset.filter(
            Q(leader=user) | Q(participants=user)
        ).distinct()


class MyGroup(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        user = request.user
        return queryset.filter(
            Q(band__leader=user) | Q(band__participants=user)
        ).distinct()
