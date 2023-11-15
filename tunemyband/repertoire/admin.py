from django.contrib import admin
from .models import Composition, Author, Genre
# Adaptation, MusicalPart

admin.site.register(Genre)
admin.site.register(Composition)
admin.site.register(Author)
# admin.site.register(Adaptation)
# admin.site.register(MusicalPart)

