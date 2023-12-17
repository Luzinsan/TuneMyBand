from django.contrib import admin
from .models import accounts, profile, dicts, equipments


@admin.register(dicts.TypeEquipment)
class TypeEquipmentAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class SkillInline(admin.StackedInline):
    model = dicts.Skill
    fields = ('code', 'name', 'sort', 'is_active',)


class GenreInline(admin.StackedInline):
    model = dicts.Genre
    fields = ('code', 'name', 'sort', 'is_active',)


class ProfileInline(admin.StackedInline):
    model = profile.Profile
    fields = ('photo', 'birthday', 'sex', 'skills', 'genres', 'about',)
    inlines = (
        SkillInline,
        GenreInline
    )


class EquipmentInline(admin.TabularInline):
    model = equipments.Equipment
    fields = ('owner', 'name', 'type', 'status', 'description',)


@admin.register(accounts.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'email',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    list_filter = ('date_joined', )
    inlines = (
        ProfileInline,
    )


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

