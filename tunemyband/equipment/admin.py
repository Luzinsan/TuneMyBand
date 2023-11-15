from django.contrib import admin
from .models import Equipment


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('owner', 'name', 'state', 'register_date')
    list_display_links = ('name',)


