from django.contrib import admin
from .models import Event, Performance


@admin.register(Performance)
class PerformanceAdmin(admin.ModelAdmin):
    pass


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_datetime', 'end_datetime', 'place', 'level', 'description', 'sponsor')
    list_display_links = ('start_datetime', 'end_datetime', 'description', 'sponsor')
    search_fields = ('name', 'place', 'level', 'start_datetime', 'description', 'sponsor')
    list_editable = ('name', 'place', 'level')
    list_filter = ('level', )
    fields = ['name', ('start_datetime', 'end_datetime'), ('place', 'level'), 'description', 'sponsor']

