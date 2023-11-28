from django.contrib import admin
from .models import Rehearsal


@admin.register(Rehearsal)
class RehearsalAdmin(admin.ModelAdmin):
    list_display = ('music_band', 'start_date', 'end_time', 'place', 'description')
    list_display_links = ('start_date', )
