from django.contrib.auth import get_user_model
from django.db import models
User = get_user_model()


class Song(models.Model):
    title = models.CharField('Название', max_length=20, )
    group = models.ForeignKey('bands.Group', models.CASCADE, 'songs_groups',
                              verbose_name='Группа', )
    file = models.FileField('Файл аранжировки', null=True, blank=True, )
    duration = models.DurationField('Продолжительность песни', null=True, blank=True, )
    genres = models.ManyToManyField('bands.Genre', 'songs',
                               verbose_name='Жанры')

    def __str__(self):
        return f'{self.group} ({self.group.pk}) - {self.title}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'group'], name='unique_group_song')
        ]
        verbose_name = 'Музыкальное произведение'
        verbose_name_plural = 'Музыкальные произведения'


class MusicPart(models.Model):
    song = models.ForeignKey('bands.Song', models.CASCADE, 'parts_songs',
                             verbose_name='Музыкальное произведение', )
    instrument = models.ForeignKey('bands.Equipment', models.CASCADE, 'parts_instruments',
                                   verbose_name='Инструмент', )
    name = models.CharField('Название', max_length=30, )
    file = models.FileField('Файл партитуры', null=True, blank=True, )

    def __str__(self):
        return f'{self.song} - {self.instrument} - {self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['song', 'instrument', 'name', ], name='unique_song_instrument_part')
        ]
        verbose_name = 'Партия произведения'
        verbose_name_plural = 'Партии произведений'
