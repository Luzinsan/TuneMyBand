from django.contrib import admin
from .models import bands, equipments, \
    repertoires, events, rehearsals


@admin.register(bands.Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('created_date', 'name', 'leader', )
    search_fields = ('name', 'leader', )
    list_editable = ('name', )
    list_filter = ('created_date', )


@admin.register(bands.Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('band', 'name', 'manager', )
    search_fields = ('band', 'name', 'manager', )
    list_editable = ('name', 'manager', )
    list_filter = ('manager', )


@admin.register(equipments.TypeEquipment)
class TypeEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


@admin.register(equipments.Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'type', 'status', 'description', )
    search_fields = ('owner', 'name', 'type', 'description', )
    list_editable = ('name', 'description', )
    list_filter = ('type', )


@admin.register(repertoires.Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('group', 'title', 'file', 'duration', )
    search_fields = ('title', 'group', 'file', )
    list_editable = ('title', 'duration',)
    list_filter = ('duration',)


@admin.register(repertoires.MusicPart)
class MusicPartAdmin(admin.ModelAdmin):
    list_display = ('song', 'instrument', 'name', 'file', )
    search_fields = ('song', 'instrument', 'name', 'file', )
    list_editable = ('instrument', 'name', )
    list_filter = ('instrument', )


@admin.register(events.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time_start', 'time_end', 'place', 'level', 'description', )
    search_fields = ('name', 'place', 'description', )
    list_editable = ('place', 'description',)
    list_filter = ('level',)


@admin.register(events.Performance)
class PerformanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'song', 'group', )
    search_fields = ('event', 'song', 'group', )
    list_filter = ('event', 'group', )


@admin.register(rehearsals.Rehearsal)
class RehearsalAdmin(admin.ModelAdmin):
    list_display = ('group', 'date', 'time_start', 'time_end', 'description', )
    search_fields = ('group', 'date', 'description', )
    list_editable = ('date', 'time_start', 'time_end', )
    list_filter = ('group', 'date', )
