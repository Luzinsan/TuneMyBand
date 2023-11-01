from django.conf import settings
from django.db import models
from django.utils import timezone
# from ..repertoire.models import Composition

# TODO: add place by googlw map api https://stackoverflow.com/questions/48388366/i-want-to-add-a-location-field-in-django-model-which-take-location-input-by-putt


class Event(models.Model):
    name = models.CharField(db_index=True, max_length=100)
    date = models.DateField(db_index=True)
    # place = models.
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(null=True, blank=True)

    LEVELS = \
        (
            ('6', 'Школьный'),
            ('5', 'Студенческий'),
            ('4', 'Городской'),
            ('3', 'Областной'),
            ('2', 'Федеральный'),
            ('1', 'Мировой')
        )
    level = models.CharField(max_length=1, choices=LEVELS)
    sponsor = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name} - {self.date}'


class Performance(models.Model):
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE, primary_key=True)
    serial_number = models.PositiveSmallIntegerField()
    # composition = models.ForeignKey(to='Composition', on_delete=models.CASCADE)
    artists = models.ManyToManyField(to=settings.AUTH_USER_MODEL)

    def __str__(self):
        return f'{self.event.name}|{self.composition.name}'
