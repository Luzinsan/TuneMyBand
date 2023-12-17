from django.contrib import admin
from .models import accounts, profile, dicts


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


@admin.register(accounts.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'email',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    list_filter = ('date_joined', )
    inlines = (
        ProfileInline,
    )

