from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Event(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    date = models.DateField(null=False, blank=False, verbose_name='Дата')
    time_start = models.TimeField(null=False, blank=False, verbose_name='Время начала')
    time_end = models.TimeField(null=True, blank=True, verbose_name='Время окончания')
    place = models.CharField(max_length=100, verbose_name='Место проведения')
    description = models.TextField(null=True, blank=True, max_length=500, verbose_name='Описание')
    level = models.ForeignKey('bands.Level', models.RESTRICT, 'events_levels', verbose_name='Уровень', )

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
    event = models.ForeignKey('bands.Event', models.CASCADE, 'performances_events', verbose_name='Мероприятие', )
    song = models.ForeignKey('bands.Song', models.CASCADE, 'performances_songs', verbose_name='Музыкальное произведение', )
    group = models.ForeignKey('bands.Group', models.CASCADE, 'performances_groups', verbose_name='Музыкальная группа', )
    artists = models.ManyToManyField(User, 'performances_users', verbose_name='Исполнители', )

    def __str__(self):
        return f'{self.event} - {self.song} - {self.group} - {self.artist}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['event', 'song', 'group',], name='unique_performance')
        ]
        ordering = ['-event', 'group', ]
        verbose_name = 'Выступление'
        verbose_name_plural = 'Выступления'
