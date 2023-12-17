from django.contrib import admin
from django.db.models import Count
from django.urls import reverse
from django.utils.html import format_html

from .models import bands, equipments, \
    repertoires, events, rehearsals, dicts


#######################################################
# INLINES
#######################################################
class BandInline(admin.TabularInline):
    model = bands.Band
    fields = ('name', 'leader', )


class GroupInline(admin.TabularInline):
    model = bands.Group
    fields = ('name', 'band', 'manager', 'members', )


class EquipmentInline(admin.TabularInline):
    model = equipments.Equipment
    fields = ('owner', 'name', 'type', 'status', 'description',)


class PerformanceInline(admin.TabularInline):
    model = events.Performance
    fields = ('event', 'group', 'song', 'artists',)


class RehearsalInline(admin.TabularInline):
    model = rehearsals.Rehearsal
    fields = ('group', 'date', 'time_start', 'time_end', 'members', 'description',)


class SongInline(admin.TabularInline):
    model = repertoires.Song
    fields = ('title', 'group', 'file', 'duration',)


class MusicPartInline(admin.TabularInline):
    model = repertoires.MusicPart
    fields = ('song', 'instrument', 'name', 'file',)


#######################################################
# MODELS
#######################################################
@admin.register(bands.Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'name', 'leader', 'members_count', )
    search_fields = ('name', )
    list_editable = ('name',)
    list_filter = ('created_date',)
    inlines = (
        GroupInline,
    )
    autocomplete_fields = ('leader',)
    filter_horizontal = ('members',)

    def members_count(self, obj):
        return obj.members_count
    members_count.short_description = 'Количество участников'

    def get_queryset(self, request):
        queryset = bands.Band.objects.annotate(
            members_count=Count('members')
        )
        return queryset


@admin.register(bands.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('band_link', 'name', 'manager', 'members_count',)
    search_fields = ('band', 'name', 'manager',)
    list_editable = ('manager',)
    list_display_links = ('name',)
    list_filter = ('manager',)
    autocomplete_fields = ('band', 'manager',)
    list_select_related = ('band',)
    inlines = (
        PerformanceInline,
        RehearsalInline,
        SongInline,
    )
    filter_horizontal = ('members',)

    def members_count(self, obj):
        return obj.members_count

    members_count.short_description = 'Количество участников'

    def get_queryset(self, request):
        queryset = bands.Group.objects.annotate(
            members_count=Count('members')
        )
        return queryset

    def band_link(self, obj):
        link = reverse(
            'admin:bands_band_change', args=[obj.band.id]
        )
        return format_html('<a href="{}">{}</a>', link, obj.band)


@admin.register(dicts.TypeEquipment)
class TypeEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(dicts.Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(equipments.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'type', 'status', 'description',)
    search_fields = ('owner', 'name', 'type', 'description',)
    list_editable = ('name', 'description',)
    list_filter = ('type',)
    autocomplete_fields = ('owner',)
    list_select_related = ('owner', 'type')
    radio_fields = {
        'type': admin.VERTICAL,
    }


@admin.register(repertoires.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('group', 'title', 'file', 'duration',)
    search_fields = ('title', 'group', 'file',)
    list_editable = ('title', 'duration',)
    list_filter = ('duration',)
    inlines = (
        MusicPartInline,
    )
    autocomplete_fields = ('group',)
    list_select_related = ('group', )
    filter_horizontal = ('genres',)


@admin.register(repertoires.MusicPart)
class MusicPartAdmin(admin.ModelAdmin):
    list_display = ('song', 'instrument', 'name', 'file',)
    search_fields = ('song', 'instrument', 'name', 'file',)
    list_editable = ('instrument', 'name',)
    list_filter = ('instrument',)
    autocomplete_fields = ('song', 'instrument')
    list_select_related = ('song', 'instrument')


@admin.register(events.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time_start', 'time_end', 'place', 'level',)
    search_fields = ('name', 'place',)
    list_editable = ('place',)
    list_filter = ('level',)
    inlines = (
        PerformanceInline,
    )
    radio_fields = {
        'level': admin.VERTICAL,
    }


@admin.register(events.Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('event_link', 'song', 'group',)
    search_fields = ('event', 'song', 'group',)
    list_filter = ('event', 'group',)
    autocomplete_fields = ('event', 'song', 'group',)
    list_select_related = ('event', 'song', 'group', )
    filter_horizontal = ('artists',)

    def event_link(self, obj):
        link = reverse(
            'admin:bands_event_change', args=[obj.event.id]
        )
        return format_html('<a href="{}">{}</a>', link, obj.event)


@admin.register(rehearsals.Rehearsal)
class RehearsalAdmin(admin.ModelAdmin):
    list_display = ('group', 'date', 'time_start', 'time_end', 'description',)
    search_fields = ('group', 'date', 'description',)
    list_editable = ('date', 'time_start', 'time_end',)
    list_filter = ('group', 'date',)
    autocomplete_fields = ('group', )
    list_select_related = ('group', )
    filter_vertical = ('members',)
