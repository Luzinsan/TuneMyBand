from django.contrib.auth import get_user_model
from django.db import models
from . import bands, equipments
User = get_user_model()


class Song(models.Model):
    title = models.CharField(max_length=20, verbose_name='Название произведения', )
    group = models.ForeignKey(bands.Group, models.CASCADE)
    file = models.FileField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)

    def __str__(self):
        return f'{self.group} ({self.group.pk}) - {self.title}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'group'], name='unique_group_song')
        ]
        verbose_name = 'Музыкальное произведение'
        verbose_name_plural = 'Музыкальные произведения'


class MusicPart(models.Model):
    song = models.ForeignKey('bands.Song', models.CASCADE, 'parts')
    instrument = models.ForeignKey(equipments.TypeEquipment, models.CASCADE, 'parts')
    name = models.CharField(max_length=30)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return f'{self.song} - {self.instrument} - {self.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['song', 'instrument', 'name', ], name='unique_song_instrument_part')
        ]
        verbose_name = 'Партия произведения'
        verbose_name_plural = 'Партии произведений'
