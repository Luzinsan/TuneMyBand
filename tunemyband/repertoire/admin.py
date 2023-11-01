from django.contrib import admin
from .models import Composition, Author, Adaptation, MusicalPart, Genre

admin.site.register(Genre)
admin.site.register(Composition)
admin.site.register(Author)
admin.site.register(Adaptation)
admin.site.register(MusicalPart)

