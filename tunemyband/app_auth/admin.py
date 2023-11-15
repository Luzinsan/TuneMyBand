from django.contrib import admin
from .models import CustomUser


# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('sex', 'birthday', 'about')
#     list_display_links = ('about', )
#     search_fields = ('sex', 'birthday')
#

admin.site.register(CustomUser)
