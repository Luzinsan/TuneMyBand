from django.conf import settings
from django.db import models
from django.utils import timezone
from viewflow.fields import CompositeKey


class Genre(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Author(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return self.name


class Composition(models.Model):
    # id = CompositeKey(columns=['name', 'authors'])
    name = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, blank=True)

    create_date = models.DateTimeField(null=True, blank=True)
    release_date = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField()
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f'{self.name}'


# class Adaptation(models.Model):
#     original = models.ForeignKey(to=Composition, on_delete=models.CASCADE)
#     duration = models.DurationField()
#     genres = models.ManyToManyField(Genre)
#     file = models.FileField(null=True, blank=True)


# class MusicalPart(models.Model):
#     adaptation = models.ForeignKey(Adaptation, on_delete=models.CASCADE)
#     # instrument = models.ForeignKey(Equipment, on_delete=models.SET_NULL, null=True)
#     file = models.FileField(null=True, blank=True)

