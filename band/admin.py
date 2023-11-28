from django.contrib import admin
from .models import MusicBand


@admin.register(MusicBand)
class MusicBandAdmin(admin.ModelAdmin):
    list_display = ('register_date', 'name', 'url', 'date_created')
    search_fields = ('name',)
    list_editable = ('name',)
    list_filter = ('register_date', 'date_created')
    fields = ['name', ('url', 'date_created')]

