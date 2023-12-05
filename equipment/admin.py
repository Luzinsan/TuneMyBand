from django.contrib import admin
from .models import Equipment, TypeOfEquipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'type', 'state', 'register_date')
    list_display_links = ('name',)
    list_filter = ('state', )
    fieldsets = (
        (None, {
            'fields': ('owner', 'name', 'type', 'register_date')
        }),
        ('Доступность', {
            'fields': ('state', 'music_band_show')
        }),
        ('Другое', {
            'fields': ('description',)
        })
    )


admin.site.register(TypeOfEquipment)
