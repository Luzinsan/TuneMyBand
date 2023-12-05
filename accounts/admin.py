from django.contrib import admin
from .models import Skills, Genre, User

admin.site.register(User)
admin.site.register(Skills)
admin.site.register(Genre)


# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     pass
