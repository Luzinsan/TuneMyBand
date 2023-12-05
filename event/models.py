from django.conf import settings
from django.db import models
from django.utils import timezone
from accounts.models import User
from repertoire.models import Adaptation
from band.models import MusicBand


class Event(models.Model):
    name = models.CharField(max_length=100)
    start_datetime = models.DateTimeField(null=False, blank=False)
    place = models.CharField(max_length=100)
    end_datetime = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=500)
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
    sponsor = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name}|{self.start_datetime}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'start_datetime'], name='unique_event')
        ]
        ordering = ['-start_datetime', 'name']
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Performance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    composition = models.ForeignKey(Adaptation, on_delete=models.CASCADE)
    music_band = models.ForeignKey(MusicBand, on_delete=models.CASCADE)
    artists = models.ManyToManyField(User, blank=False)

    def __str__(self):
        return f'{self.event}|{self.composition}|{self.music_band}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['event', 'composition', 'music_band'], name='unique_performance')
        ]
        ordering = ['-event__start_datetime', 'music_band__name', 'composition__original__title', ]
        verbose_name = 'Выступление'
        verbose_name_plural = 'Выступления'
