from django.db import models
from django.utils import timezone
from filer.fields.file import FilerFileField

from band.models import MusicBand


class Genre(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class Original(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, verbose_name='Имя исполнителя, группы или коллаборация')

    release_date = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)

    def __str__(self):
        return f'{self.title}/{self.author}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['title', 'author'], name='unique_original_title_author')
        ]


class Adaptation(models.Model):
    original = models.ForeignKey(to=Original, on_delete=models.CASCADE)
    music_band = models.ForeignKey(to=MusicBand, on_delete=models.CASCADE)
    duration = models.DurationField(null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    file = FilerFileField(null=True, blank=True, related_name='adaptation_file',
                          on_delete=models.SET_NULL)
    musical_parts = FilerFileField(null=True, blank=True, related_name='adaptation_musical_parts',
                                   on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.original}|{self.music_band}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['original', 'music_band', 'file'], name='unique_adaptation')
        ]
