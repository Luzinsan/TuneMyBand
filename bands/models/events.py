from django.db import models
from django.contrib.auth import get_user_model
from . import repertoires, bands
User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(null=False, blank=False)
    time_start = models.TimeField(null=False, blank=False)
    time_end = models.TimeField(null=True, blank=True)
    place = models.CharField(max_length=100)
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
    level = models.CharField(max_length=1, choices=LEVELS, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.date} - {self.time_start}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'date', 'time_start', 'place', ],
                                    name='unique_event')
        ]
        ordering = ['-date', 'time_start']
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'


class Performance(models.Model):
    event = models.ForeignKey(Event, models.CASCADE, 'performances', )
    song = models.ForeignKey(repertoires.Song, models.CASCADE, 'performances', )
    group = models.ForeignKey(bands.Group, models.CASCADE, 'performances', )
    artists = models.ManyToManyField(User, 'performances', blank=False, )

    def __str__(self):
        return f'{self.event} - {self.song} - {self.group}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['event', 'song', 'group'], name='unique_performance')
        ]
        ordering = ['-event', 'group', ]
        verbose_name = 'Выступление'
        verbose_name_plural = 'Выступления'
