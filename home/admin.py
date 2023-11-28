from django.contrib import admin
from .models import Skills, Genre, Profile


admin.site.register(Skills)
admin.site.register(Genre)
# admin.site.register(AlterUser)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
