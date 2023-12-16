from django.contrib import admin
from .models import accounts, profile


class ProfileInline(admin.StackedInline):
    model = profile.Profile
    fields = ('photo', 'birthday', 'sex', 'skills', 'genres', 'about',)
    filter_horizontal = ('skills', 'genres',)


@admin.register(accounts.User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'phone_number', 'email',)
    search_fields = ('username', 'first_name', 'last_name', 'email',)
    list_filter = ('date_joined', )
    inlines = (
        ProfileInline,
    )


