from django.db import models
from django.utils import timezone

from band.models import MusicBand
from home.models import Genre
from equipment.models import TypeOfEquipment


class Original(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, verbose_name='Имя исполнителя, группы или коллаборация')

    release_date = models.DateField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True,  related_name='original_genres', related_query_name='genre')

    def __str__(self):
        return f'{self.title}/{self.author}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique_original_title_author')
        ]
        verbose_name = 'Оригинал произведения'
        verbose_name_plural = 'Оригинальные произведения'


class Adaptation(models.Model):
    original = models.ForeignKey(to=Original, on_delete=models.CASCADE)
    music_band = models.ForeignKey(to=MusicBand, on_delete=models.CASCADE)
    duration = models.DurationField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    file = models.FileField(null=True, blank=True)

    def __str__(self):
        return f'{self.original}|{self.music_band}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['original', 'music_band', 'file'], name='unique_adaptation')
        ]
        verbose_name = 'Аранжировка'
        verbose_name_plural = 'Аранжировки'


class MusicPart(models.Model):
    adaptation = models.ForeignKey(to=Adaptation, on_delete=models.CASCADE)
    instrument = models.ForeignKey(TypeOfEquipment, on_delete=models.SET_DEFAULT, default='Неизвестно')
    musical_part = models.FileField(null=False, blank=False)

    def __str__(self):
        return f'{self.adaptation}|{self.musical_part.name}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['adaptation', 'musical_part'], name='unique_musical_part')
        ]
        verbose_name = 'Партия аранжировки'
        verbose_name_plural = 'Партии аранжировки'
