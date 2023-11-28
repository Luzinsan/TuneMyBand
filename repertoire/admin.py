from django.contrib import admin
from .models import Original, Adaptation, MusicPart


@admin.register(MusicPart)
class MusicPartAdmin(admin.ModelAdmin):
    list_display = ('adaptation', 'instrument', 'musical_part')
    list_display_links = ('adaptation',)
    list_filter = ('instrument__name',)


class MusicPartInline(admin.TabularInline):
    model = MusicPart
    extra = 0


@admin.register(Adaptation)
class AdaptationAdmin(admin.ModelAdmin):
    list_display = ('original', 'music_band', 'duration', 'file')
    inlines = [MusicPartInline]


class AdaptationInline(admin.TabularInline):
    model = Adaptation
    extra = 0


@admin.register(Original)
class OriginalAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'release_date', 'duration',)
    inlines = [AdaptationInline]
