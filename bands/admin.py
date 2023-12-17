from django.contrib import admin

from breaks.models.replacements import GroupInfo
from bands.models import bands, groups, dicts, offers


##############################
# INLINES
##############################
class ParticipantInline(admin.TabularInline):
    model = bands.Participant
    fields = ('user', 'position', 'date_joined',)


class OfferInline(admin.TabularInline):
    model = offers.Offer
    fields = ('org_accept', 'user', 'user_accept',)


class MemberInline(admin.TabularInline):
    model = groups.Member
    fields = ('participant', 'date_joined',)


class ProfileBreakInline(admin.StackedInline):
    model = GroupInfo
    fields = (
        'min_active',
        'break_start',
        'break_end',
        'break_max_duration',
    )


##############################
# MODELS
##############################
@admin.register(dicts.Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = (
        'code', 'name', 'sort', 'is_active',
    )


@admin.register(bands.Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'leader',)
    filter_vertical = ('participants',)
    inlines = (ParticipantInline, OfferInline,)
    readonly_fields = (
        'created_at', 'created_by', 'updated_at', 'updated_by',
    )


@admin.register(groups.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'manager', )
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    inlines = (
        ProfileBreakInline,
        MemberInline,
    )
    readonly_fields = (
        'created_at', 'created_by', 'updated_at', 'updated_by',
    )


@admin.register(offers.Offer)
class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'band', 'org_accept', 'user', 'user_accept',)
    search_fields = ('band__name', 'user__last_name',)

    readonly_fields = (
        'created_at', 'created_by', 'updated_at', 'updated_by',
    )
