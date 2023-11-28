from django.contrib import admin
from .models import Original, Adaptation, MusicPart

admin.site.register(Original)
admin.site.register(Adaptation)


@admin.register(MusicPart)
class MusicPartAdmin(admin.ModelAdmin):
    list_display = ('adaptation', 'instrument', 'musical_parts')
    list_display_links = ('adaptation',)
