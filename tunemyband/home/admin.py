from django.contrib import admin
from .models import MusicBand, UserProfile, Skills


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'sex', 'birthday', 'about')
    list_display_links = ('user', 'about')
    search_fields = ('sex', 'birthday')


admin.site.register(MusicBand)
admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Skills)
